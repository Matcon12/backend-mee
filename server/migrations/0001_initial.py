# Generated by Django 4.2.7 on 2023-11-21 11:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMaster',
            fields=[
                ('cust_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('cust_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_addr1', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_addr2', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_city', models.CharField(blank=True, max_length=15, null=True)),
                ('cust_st_code', models.IntegerField(blank=True, null=True)),
                ('cust_st_name', models.CharField(blank=True, max_length=20, null=True)),
                ('cust_pin', models.CharField(blank=True, max_length=6, null=True)),
                ('cust_gst_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'customer_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GstRates',
            fields=[
                ('cgst_rate', models.IntegerField(blank=True, null=True)),
                ('sgst_rate', models.IntegerField(blank=True, null=True)),
                ('igst_rate', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'gst_rates',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GstStateCode',
            fields=[
                ('state_code', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'gst_state_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MatCompanies',
            fields=[
                ('mat_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('mat_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mat_address', models.CharField(blank=True, max_length=50, null=True)),
                ('mat_gst_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_acc_no', models.CharField(blank=True, max_length=15, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=30, null=True)),
                ('bank_address', models.CharField(blank=True, max_length=50, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('fin_yr', models.CharField(blank=True, max_length=10, null=True)),
                ('last_gcn_no', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mat_companies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OtwDc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_code', models.CharField(max_length=3)),
                ('gcn_no', models.CharField(max_length=15)),
                ('gcn_date', models.DateField(default=django.utils.timezone.now)),
                ('grn_no', models.CharField(blank=True, max_length=20, null=True)),
                ('grn_date', models.DateField(default=django.utils.timezone.now)),
                ('po_no', models.CharField(max_length=15)),
                ('po_date', models.DateField(default=django.utils.timezone.now)),
                ('receiver_id', models.CharField(blank=True, max_length=4, null=True)),
                ('consignee_id', models.CharField(blank=True, max_length=4, null=True)),
                ('po_sl_no', models.IntegerField()),
                ('part_id', models.CharField(blank=True, max_length=15, null=True)),
                ('part_name', models.CharField(blank=True, max_length=50, null=True)),
                ('qty_delivered', models.IntegerField(blank=True, null=True)),
                ('uom', models.CharField(blank=True, max_length=5, null=True)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('taxable_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cgst_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sgst_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('igst_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rejected_item', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'otw_dc',
                'managed': True,
                'unique_together': {('mat_code', 'gcn_no', 'po_no', 'po_sl_no')},
            },
        ),
        migrations.CreateModel(
            name='InwDc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grn_no', models.CharField(max_length=20)),
                ('grn_date', models.DateField(default=django.utils.timezone.now)),
                ('rework_dc', models.BooleanField(default=False)),
                ('po_no', models.CharField(max_length=20)),
                ('po_date', models.DateField(default=django.utils.timezone.now)),
                ('receiver_id', models.CharField(blank=True, max_length=10, null=True)),
                ('consignee_id', models.CharField(blank=True, max_length=10, null=True)),
                ('po_sl_no', models.IntegerField()),
                ('cust_id', models.CharField(blank=True, max_length=4, null=True)),
                ('part_id', models.CharField(blank=True, max_length=20, null=True)),
                ('part_name', models.CharField(blank=True, max_length=100, null=True)),
                ('qty_received', models.IntegerField(blank=True, null=True)),
                ('purpose', models.CharField(blank=True, max_length=50, null=True)),
                ('uom', models.CharField(blank=True, max_length=10, null=True)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('qty_delivered', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('qty_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'inw_dc',
                'managed': True,
                'unique_together': {('grn_no', 'po_no', 'po_sl_no')},
            },
        ),
        migrations.CreateModel(
            name='Po',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('po_no', models.CharField(max_length=20)),
                ('po_date', models.DateField(default=django.utils.timezone.now)),
                ('open_po', models.BooleanField(default=False)),
                ('open_po_validity', models.DateField(blank=True, null=True)),
                ('quote_ref_no', models.CharField(blank=True, max_length=5, null=True)),
                ('receiver_id', models.CharField(blank=True, max_length=4, null=True)),
                ('consignee_id', models.CharField(blank=True, max_length=4, null=True)),
                ('po_sl_no', models.IntegerField()),
                ('part_id', models.CharField(blank=True, max_length=20, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('qty_sent', models.IntegerField(blank=True, null=True)),
                ('uom', models.CharField(blank=True, max_length=5, null=True)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cust_id', models.ForeignKey(blank=True, db_column='cust_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='server.customermaster')),
            ],
            options={
                'db_table': 'po',
                'managed': True,
                'unique_together': {('po_no', 'po_sl_no')},
            },
        ),
        migrations.CreateModel(
            name='PartMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('part_id', models.CharField(max_length=20)),
                ('part_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_id', models.ForeignKey(blank=True, db_column='cust_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='server.customermaster')),
            ],
            options={
                'db_table': 'part_master',
                'managed': True,
                'unique_together': {('part_id', 'cust_id')},
            },
        ),
    ]
