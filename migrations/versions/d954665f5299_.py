"""empty message

Revision ID: d954665f5299
Revises: 8a9df5acf5f8
Create Date: 2024-09-08 10:49:36.579613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd954665f5299'
down_revision = '8a9df5acf5f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_closed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grant', schema=None) as batch_op:
        batch_op.drop_column('is_closed')

    # ### end Alembic commands ###
