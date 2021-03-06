"""Candidate result

Revision ID: 135fa0b0bde1
Revises: 2c7d7b3b6efa
Create Date: 2021-05-04 21:40:23.917848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '135fa0b0bde1'
down_revision = '2c7d7b3b6efa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidate', sa.Column('result', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('candidate', 'result')
    # ### end Alembic commands ###
