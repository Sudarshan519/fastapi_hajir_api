"""leave request

Revision ID: 3060c5282721
Revises: 
Create Date: 2023-07-18 22:50:32.152093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3060c5282721'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_id', table_name='user')
    op.drop_table('user')
    op.add_column('companymodel', sa.Column('total_casual_leave_in_year', sa.Integer(), nullable=True))
    op.add_column('companymodel', sa.Column('total_sick_leave_in_year', sa.Integer(), nullable=True))
    op.add_column('employeemodel', sa.Column('total_sick_leave_taken', sa.Integer(), nullable=True))
    op.add_column('employeemodel', sa.Column('total_casual_leave_taken', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employeemodel', 'total_casual_leave_taken')
    op.drop_column('employeemodel', 'total_sick_leave_taken')
    op.drop_column('companymodel', 'total_sick_leave_in_year')
    op.drop_column('companymodel', 'total_casual_leave_in_year')
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=60), nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=256), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###