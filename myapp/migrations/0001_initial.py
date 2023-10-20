# Generated by Django 4.2.6 on 2023-10-20 09:01

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(default='category-title', max_length=128)),
                ('slug', models.SlugField(default='category-slug', max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('sub_description', models.TextField(blank=True)),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('status', models.CharField(db_index=True, default='NORMAL', max_length=32)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=64)),
                ('user_agent', models.TextField(blank=True)),
                ('accept_language', models.TextField(blank=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('payment_method', models.IntegerField(db_index=True)),
                ('transaction_id', models.CharField(blank=True, max_length=64)),
                ('status', models.IntegerField(db_index=True)),
                ('visible', models.IntegerField(db_index=True)),
                ('total_list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('message', models.TextField(blank=True)),
                ('suspicious', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'pincoin order',
                'verbose_name_plural': 'pincoin orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
                'db_table': 'order_item',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(default='product-slug', max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('position', models.IntegerField(default=0)),
                ('status', models.IntegerField(db_index=True, default=0)),
                ('stock', models.IntegerField(db_index=True, default=0)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('minimum_stock_level', models.IntegerField(default=0)),
                ('maximum_stock_level', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=64)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('status', models.IntegerField(db_index=True, default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.product')),
            ],
            options={
                'verbose_name': 'voucher',
                'verbose_name_plural': 'vouchers',
                'db_table': 'voucher',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.IntegerField(db_index=True, default=0)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.role')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_verified', models.BooleanField(default=False)),
                ('phone_verified_status', models.IntegerField(db_index=True, default=0)),
                ('document_verified', models.BooleanField(default=False)),
                ('allow_order', models.BooleanField(default=False)),
                ('photo_id', models.CharField(blank=True, max_length=256, null=True)),
                ('card', models.CharField(blank=True, max_length=256, null=True)),
                ('total_order_count', models.IntegerField(default=0)),
                ('first_purchased', models.DateTimeField(null=True)),
                ('last_purchased', models.DateTimeField(null=True)),
                ('not_purchased_months', models.BooleanField(default=False)),
                ('repurchased', models.DateTimeField(null=True)),
                ('max_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('total_list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('average_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('mileage', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('memo', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(db_index=True, default=0, null=True)),
                ('domestic', models.IntegerField(db_index=True, default=0, null=True)),
                ('telecom', models.CharField(blank=True, max_length=16, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('account', models.IntegerField(db_index=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('received', models.DateTimeField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'order payment',
                'verbose_name_plural': 'order payments',
                'db_table': 'order_payment',
            },
        ),
        migrations.CreateModel(
            name='OrderItemVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=64)),
                ('revoked', models.BooleanField(default=False)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.orderitem')),
                ('voucher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.voucher')),
            ],
            options={
                'verbose_name': 'order item voucher',
                'verbose_name_plural': 'order item vouchers',
                'db_table': 'order_item_voucher',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.user'),
        ),
        migrations.CreateModel(
            name='CategoryTreePath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('path_length', models.IntegerField(default=0)),
                ('ancestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ancestors', to='myapp.category')),
                ('descendant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descendants', to='myapp.category')),
            ],
            options={
                'verbose_name': 'category tree path',
                'verbose_name_plural': 'category tree paths',
                'db_table': 'category_tree_path',
            },
        ),
        migrations.AddIndex(
            model_name='voucher',
            index=models.Index(fields=['code'], name='voucher_code_8bda2a_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='voucher',
            unique_together={('product', 'code')},
        ),
    ]
