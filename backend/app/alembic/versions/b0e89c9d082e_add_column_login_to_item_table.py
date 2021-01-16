"""Add column login to item table

Revision ID: b0e89c9d082e
Revises: d4867f3a4c0a
Create Date: 2021-01-15 17:33:04.688509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0e89c9d082e'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('login', sa.String(), nullable=True))
    op.add_column('item', sa.Column('password', sa.String(), nullable=True))
    op.create_index(op.f('ix_item_login'), 'item', ['login'], unique=False)
    op.create_index(op.f('ix_item_password'), 'item', ['password'], unique=False)
    op.drop_index('ix_item_title', table_name='item')
    op.drop_column('item', 'title')
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('item', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_item_title', 'item', ['title'], unique=False)
    op.drop_index(op.f('ix_item_password'), table_name='item')
    op.drop_index(op.f('ix_item_login'), table_name='item')
    op.drop_column('item', 'password')
    op.drop_column('item', 'login')
    # ### end Alembic commands ###