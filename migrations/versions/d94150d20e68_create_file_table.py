"""Create file table

Revision ID: d94150d20e68
Revises: 
Create Date: 2024-01-08 12:02:02.288985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd94150d20e68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('size', sa.BigInteger(), nullable=True),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('mime_type', sa.String(length=50), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    # ### end Alembic commands ###
