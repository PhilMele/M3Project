"""Fix relationship warnings

Revision ID: b9dda11bef3b
Revises: 30dd99ec2bf1
Create Date: 2024-08-01 10:12:39.920350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9dda11bef3b'
down_revision = '30dd99ec2bf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grant_question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer, nullable=False, constraint_name='fk_grant_question_user')) 
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grant_question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
