"""Add Grant model

Revision ID: 4b629eab2e0b
Revises: d5c3c14bc4c0
Create Date: 2024-08-01 13:21:59.492119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b629eab2e0b'
down_revision = 'd5c3c14bc4c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grant_title', sa.String(length=200), nullable=False),
    sa.Column('grant_description', sa.String(length=200), nullable=False),
    sa.Column('grant_fund', sa.Integer(), nullable=False),
    sa.Column('create_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('grant_description'),
    sa.UniqueConstraint('grant_title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grant')
    # ### end Alembic commands ###
