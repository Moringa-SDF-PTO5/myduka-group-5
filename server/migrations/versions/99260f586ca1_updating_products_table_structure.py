"""Updating Products table structure

Revision ID: 99260f586ca1
Revises: 4da8b0d8ecc7
Create Date: 2024-07-31 11:29:05.540328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99260f586ca1'
down_revision = '4da8b0d8ecc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number_received', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('number_dispatched', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('is_paid', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('is_paid')
        batch_op.drop_column('number_dispatched')
        batch_op.drop_column('number_received')

    # ### end Alembic commands ###
