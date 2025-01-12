"""empty message

Revision ID: ddd601b41738
Revises: 82f3835fff72
Create Date: 2024-12-01 00:51:05.651441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddd601b41738'
down_revision = '82f3835fff72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid', sa.String(length=50), nullable=True))
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('userid')

    # ### end Alembic commands ###
