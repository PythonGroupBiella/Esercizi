"""prima ver

Revision ID: 60bb41479000
Revises: 
Create Date: 2020-11-09 21:04:07.614174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60bb41479000'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('corso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('insegnante', sa.String(length=100), nullable=True),
    sa.Column('livello', sa.String(length=100), nullable=True),
    sa.Column('descrizione', sa.String(length=255), nullable=True),
    sa.Column('logo_img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('corso_tags',
    sa.Column('corso_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['corso_id'], ['corso.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('corso_id', 'tag_id')
    )
    op.create_table('serata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('descrizione', sa.String(length=255), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('link_partecipazione', sa.String(length=255), nullable=True),
    sa.Column('link_registrazione', sa.String(length=255), nullable=True),
    sa.Column('corso_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['corso_id'], ['corso.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id', 'data', name='contraint_serata')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('serata')
    op.drop_table('corso_tags')
    op.drop_table('tag')
    op.drop_table('corso')
    # ### end Alembic commands ###
