"""
Add formation column

Revision ID: 11ab56d75358
Revises: e2d140e07d12
Create Date: 2018-05-10 12:07:58.625749
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '11ab56d75358'
down_revision = 'e2d140e07d12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_connection', sa.Column('formation', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_connection', 'formation')
    # ### end Alembic commands ###
