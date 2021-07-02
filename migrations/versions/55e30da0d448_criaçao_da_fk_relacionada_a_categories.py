"""Criaçao da Fk relacionada a categories

Revision ID: 55e30da0d448
Revises: 60de4ef08327
Create Date: 2021-06-18 11:19:05.671692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55e30da0d448'
down_revision = '60de4ef08327'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_categories', sa.Column('categoryy_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'task_categories', 'categories', ['categoryy_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task_categories', type_='foreignkey')
    op.drop_column('task_categories', 'categoryy_id')
    # ### end Alembic commands ###
