"""empty message

Revision ID: 3b08b50c3288
Revises: 8840eb891e0a
Create Date: 2020-07-27 20:34:48.220151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b08b50c3288'
down_revision = '8840eb891e0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('category_description', sa.String(), nullable=False))
    op.add_column('problems', sa.Column('question_title', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('problems', 'question_title')
    op.drop_column('categories', 'category_description')
    # ### end Alembic commands ###
