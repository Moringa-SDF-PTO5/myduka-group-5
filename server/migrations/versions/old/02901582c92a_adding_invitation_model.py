"""Adding invitation model

Revision ID: 02901582c92a
Revises: 
Create Date: 2024-07-21 11:20:52.598376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02901582c92a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('username', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=120),
                              autoincrement=False, nullable=False),
                    sa.Column('password_hash', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('role', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=True),
                    sa.Column('is_active', sa.BOOLEAN(),
                              autoincrement=False, nullable=True),
                    sa.Column('confirmed_admin', sa.BOOLEAN(),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('user_id', name='user_pkey'),
                    sa.UniqueConstraint('email', name='user_email_key'),
                    sa.UniqueConstraint('username', name='user_username_key')
                    )
    op.create_table('users',
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('username', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=120),
                              autoincrement=False, nullable=False),
                    sa.Column('password_hash', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('role', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text(
                        'true'), autoincrement=False, nullable=True),
                    sa.Column('confirmed_admin', sa.BOOLEAN(), server_default=sa.text(
                        'false'), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('user_id', name='users_pkey'),
                    sa.UniqueConstraint('email', name='users_email_key'),
                    sa.UniqueConstraint('username', name='users_username_key')
                    )
    # ### end Alembic commands ###