"""Added relationship between User and Invitation

Revision ID: a1bcb8e1adc6
Revises: a5fbe4c82ed8
Create Date: 2024-07-20 17:30:59.187885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1bcb8e1adc6'
down_revision = 'a5fbe4c82ed8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    with op.batch_alter_table('invitations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invitations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

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
    # ### end Alembic commands ###
