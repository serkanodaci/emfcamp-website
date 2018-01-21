"""

Revision ID: a8b7f5ca396f
Revises: ce7241afadc2
Create Date: 2018-01-21 15:45:36.272573

"""

# revision identifiers, used by Alembic.
revision = 'a8b7f5ca396f'
down_revision = 'ce7241afadc2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('promo_opt_in', sa.Boolean(), nullable=False))

    with op.batch_alter_table('user_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('promo_opt_in', sa.Boolean(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_version', schema=None) as batch_op:
        batch_op.drop_column('promo_opt_in')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('promo_opt_in')

    # ### end Alembic commands ###