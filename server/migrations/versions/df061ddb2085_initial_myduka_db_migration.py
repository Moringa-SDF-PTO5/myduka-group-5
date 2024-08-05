"""Initial myduka db migration.

Revision ID: df061ddb2085
Revises: 
Create Date: 2024-07-15 19:13:54.097334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df061ddb2085'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('buying_price', sa.Integer(), nullable=False),
    sa.Column('selling_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('stores',
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('store_name', sa.String(length=50), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.Column('is_active', sa.Boolean(create_constraint=1), nullable=True),
    sa.Column('confirmed_admin', sa.Boolean(create_constraint=1), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('inventory',
    sa.Column('inventory_id', sa.Integer(), nullable=False),
    sa.Column('inventory_name', sa.String(length=50), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('quantity_received', sa.Integer(), nullable=True),
    sa.Column('quantity_in_stock', sa.Integer(), nullable=False),
    sa.Column('quantity_spoilt', sa.Integer(), nullable=False),
    sa.Column('payment_status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quantity_received'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('inventory_id')
    )
    op.create_table('requests',
    sa.Column('request_id', sa.Integer(), nullable=False),
    sa.Column('Inventory_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('request_date', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['Inventory_id'], ['inventory.inventory_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('request_id', 'request_date', 'status')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_table('inventory')
    op.drop_table('users')
    op.drop_table('stores')
    op.drop_table('products')
    # ### end Alembic commands ###