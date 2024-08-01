"""Edit GrantModel

Revision ID: 00625e2eebde
Revises: 4b629eab2e0b
Create Date: 2024-08-01 13:34:40.298692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00625e2eebde'
down_revision = '4b629eab2e0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_on', sa.DateTime(), nullable=True))
        batch_op.drop_column('create_on')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_on', sa.DATETIME(), nullable=True))
        batch_op.drop_column('created_on')

    # ### end Alembic commands ###
