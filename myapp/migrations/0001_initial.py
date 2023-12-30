# Generated by Django 4.2.8 on 2023-12-29 09:29

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
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.BigIntegerField(null=True)),
                ('last_modified_by', models.BigIntegerField(null=True)),
                ('id', models.BigAutoField(db_column='category_id', primary_key=True, serialize=False)),
                ('title', models.CharField(default='category-title', max_length=32)),
                ('slug', models.SlugField(default='category-slug', max_length=32, unique=True)),
                ('description', models.TextField(blank=True)),
                ('sub_description', models.TextField(blank=True)),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(default='NORMAL', max_length=32)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'shop_category',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', models.BigAutoField(db_column='order_id', primary_key=True, serialize=False)),
                ('order_uuid', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=32)),
                ('user_agent', models.TextField(blank=True)),
                ('accept_language', models.TextField(blank=True)),
                ('ip_address', models.CharField(max_length=39)),
                ('payment_method', models.CharField(default='BANK_TRANSFER', max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.CharField(default='ORDERED', max_length=16)),
                ('payment', models.CharField(default='UNPAID', max_length=16)),
                ('sending', models.CharField(default='NOT_SENT', max_length=16)),
                ('visible', models.CharField(default='VISIBLE', max_length=16)),
                ('total_list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('message', models.TextField(blank=True, null=True)),
                ('suspicious', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'pincoin order',
                'verbose_name_plural': 'pincoin orders',
                'db_table': 'shop_order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(db_column='order_item_id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('subtitle', models.CharField(blank=True, max_length=32)),
                ('slug', models.CharField(max_length=32)),
                ('list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('buying_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
                'db_table': 'shop_order_item',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.BigIntegerField(null=True)),
                ('last_modified_by', models.BigIntegerField(null=True)),
                ('id', models.BigAutoField(db_column='page_id', primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('message', models.TextField()),
                ('status', models.CharField(default='NORMAL', max_length=32)),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'db_table': 'content_page',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_by', models.BigIntegerField(null=True)),
                ('last_modified_by', models.BigIntegerField(null=True)),
                ('id', models.BigAutoField(db_column='product_id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('subtitle', models.CharField(blank=True, max_length=32)),
                ('slug', models.SlugField(default='product-slug', max_length=32, unique=True)),
                ('description', models.TextField(blank=True)),
                ('position', models.IntegerField(default=0)),
                ('status', models.CharField(default='ENABLED', max_length=16)),
                ('stock', models.CharField(default='IN_STOCK', max_length=16)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('buying_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('minimum_stock_level', models.IntegerField(default=0)),
                ('maximum_stock_level', models.IntegerField(default=0)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'shop_product',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(db_column='user_id', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(default='NORMAL', max_length=32)),
                ('role', models.CharField(default='ROLE_MEMBER', max_length=32)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', models.BigAutoField(db_column='voucher_id', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=32)),
                ('remarks', models.CharField(blank=True, max_length=16)),
                ('status', models.CharField(default='PURCHASED', max_length=16)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.product')),
            ],
            options={
                'verbose_name': 'voucher',
                'verbose_name_plural': 'vouchers',
                'db_table': 'shop_voucher',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(db_column='profile_id', primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email_verified_status', models.CharField(default='UNVERIFIED', max_length=32)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=32, null=True)),
                ('domestic', models.CharField(blank=True, max_length=32, null=True)),
                ('telecom', models.CharField(blank=True, max_length=16, null=True)),
                ('phone_verified_status', models.CharField(default='UNVERIFIED', max_length=32)),
                ('photo_id', models.CharField(blank=True, max_length=256, null=True)),
                ('card', models.CharField(blank=True, max_length=256, null=True)),
                ('document_verified_status', models.CharField(default='UNVERIFIED', max_length=32)),
                ('allow_order', models.BooleanField(default=False)),
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
                ('favorites', models.TextField(default='{}')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'auth_profile',
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(db_column='order_payment_id', primary_key=True, serialize=False)),
                ('account', models.CharField(default='KB', max_length=32)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('received', models.DateTimeField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'order payment',
                'verbose_name_plural': 'order payments',
                'db_table': 'shop_order_payment',
            },
        ),
        migrations.CreateModel(
            name='OrderItemVoucher',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(db_column='order_item_voucher_id', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=32)),
                ('revoked', models.BooleanField(default=False)),
                ('remarks', models.CharField(blank=True, max_length=32)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.orderitem')),
                ('voucher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.voucher')),
            ],
            options={
                'verbose_name': 'order item voucher',
                'verbose_name_plural': 'order item vouchers',
                'db_table': 'shop_order_item_voucher',
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
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(db_column='category_tree_path_id', primary_key=True, serialize=False)),
                ('path_length', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
                ('ancestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ancestors', to='myapp.category')),
                ('descendant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descendants', to='myapp.category')),
            ],
            options={
                'verbose_name': 'category tree path',
                'verbose_name_plural': 'category tree paths',
                'db_table': 'shop_category_tree_path',
            },
        ),
        migrations.AddIndex(
            model_name='voucher',
            index=models.Index(fields=['code'], name='shop_vouche_code_b378c1_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='voucher',
            unique_together={('product', 'code')},
        ),
    ]
