"""Added user_type to User model

Revision ID: d5c3c14bc4c0
Revises: 05748cdd7dd1
Create Date: 2024-08-01 12:45:45.724642

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd5c3c14bc4c0'
down_revision = '05748cdd7dd1'
branch_labels = None
depends_on = None

def upgrade():
    # Add the new column with a default value
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_type', sa.Enum('GRANTEE', 'GRANTER', name='usertype'), nullable=False, server_default='GRANTEE'))
        
    # Remove the default value if needed
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_type', server_default=None)

def downgrade():
    # Drop the column if rolling back
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('user_type')