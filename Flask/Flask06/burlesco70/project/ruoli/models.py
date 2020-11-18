from project import db
#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()

class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

class Ruolo(db.Model):
    __tablename__ = 'ruoli'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    # n utenti hanno un certo ruolo
    users = db.relationship('Utente', backref='ruolo', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Ruolo, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    '''
    Inserimento dei ruoli nel db; User è il default
    '''
    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Administrator': [Permission.FOLLOW, Permission.COMMENT,
                              Permission.WRITE, Permission.MODERATE,
                              Permission.ADMIN],
        }
        default_role = 'User'
        for r in roles:
            role = Ruolo.query.filter_by(name=r).first()
            if role is None:
                role = Ruolo(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Ruolo %r>' % self.name