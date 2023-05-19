"""empty message

Revision ID: e8aa3cf4b5e4
Revises: 
Create Date: 2023-05-18 08:22:35.734944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8aa3cf4b5e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('actor_id')
    )
    op.create_table('movies',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('movie_title', sa.String(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('movie_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('actors')
    # ### end Alembic commands ###
