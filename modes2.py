# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accountmaster(models.Model):
    accountid = models.IntegerField(primary_key=True)
    accountname = models.CharField(unique=True, max_length=50)
    trial_groupid_3 = models.ForeignKey('Groupmaster', models.DO_NOTHING, db_column='trial_groupid_3')
    trial_costcenter_4 = models.BooleanField()
    billwisedetail = models.BooleanField()
    creditdays = models.SmallIntegerField()
    trial_creditlimit_7 = models.DecimalField(max_digits=13, decimal_places=3)
    pricelistid = models.ForeignKey('Pricelistmaster', models.DO_NOTHING, db_column='pricelistid')
    trial_address1_9 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    trial_address3_11 = models.CharField(max_length=150)
    trial_cityid_12 = models.ForeignKey('Citymaster', models.DO_NOTHING, db_column='trial_cityid_12')
    stateid = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='stateid')
    countryid = models.ForeignKey('Countrymaster', models.DO_NOTHING, db_column='countryid')
    trial_pincode_15 = models.CharField(max_length=20)
    phone = models.CharField(max_length=35)
    trial_email_17 = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    contactperson = models.CharField(max_length=50)
    trial_contactpersonmobile_21 = models.CharField(max_length=25)
    cstno = models.CharField(max_length=30)
    vatno = models.CharField(max_length=30)
    trial_panno_24 = models.CharField(max_length=30)
    servicetaxno = models.CharField(max_length=30)
    trial_debitamount_26 = models.DecimalField(max_digits=18, decimal_places=3)
    creditamount = models.DecimalField(max_digits=18, decimal_places=3)
    isfixed = models.BooleanField()
    trial_isactive_29 = models.BooleanField()
    trial_vatclassid_30 = models.ForeignKey('Vatclassmaster', models.DO_NOTHING, db_column='trial_vatclassid_30')
    intrate = models.DecimalField(max_digits=13, decimal_places=3)
    intrateper = models.SmallIntegerField()
    trial_amfield1_33 = models.CharField(max_length=50)
    amfield2 = models.CharField(max_length=50)
    trial_amfield3_35 = models.CharField(max_length=50)
    amfield4 = models.CharField(max_length=50)
    trial_amfield5_37 = models.CharField(max_length=50)
    amfield6 = models.CharField(max_length=50)
    trial_amfield7_39 = models.CharField(max_length=50)
    amfield8 = models.CharField(max_length=50)
    amfield9 = models.CharField(max_length=50)
    trial_amfield10_42 = models.CharField(max_length=50)
    link = models.CharField(max_length=512)
    useinpayroll = models.BooleanField()
    streetnumber = models.CharField(max_length=25)
    streetid = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='streetid')
    localityid = models.ForeignKey('Localitymaster', models.DO_NOTHING, db_column='localityid')
    trial_teamid_48 = models.CharField(max_length=50)
    accountcode = models.CharField(max_length=50)
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()
    gstinno = models.CharField(max_length=20)
    teamidreport = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'accountmaster'


class Activitylog(models.Model):
    trial_logdate_1 = models.DateTimeField()
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=18, decimal_places=3)
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    trial_locationid_9 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_locationid_9')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    trial_createlocationid_11 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_createlocationid_11')
    oldvoucherdate = models.DateTimeField()
    oldvchidprefix = models.CharField(max_length=15)
    oldvchidymd = models.CharField(max_length=6)
    trial_oldvchnumber_15 = models.IntegerField()
    oldamount = models.DecimalField(max_digits=18, decimal_places=3)
    oldlocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='oldlocationid')
    oldmodifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='oldmodifylocationid')
    trial_transactiontype_19 = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='trial_transactiontype_19')
    sessionid = models.CharField(max_length=6)
    trial_logid_21 = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'activitylog'


class Activitylogmaster(models.Model):
    logid = models.BigIntegerField()
    logdate = models.DateTimeField()
    trial_userid_3 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_3')
    trial_locationid_4 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_locationid_4')
    transactiontype = models.SmallIntegerField()
    trial_sessionid_6 = models.CharField(max_length=6)
    mastertable = models.CharField(max_length=50)
    mastername = models.CharField(max_length=250)
    trial_masterid_9 = models.CharField(max_length=50)
    oldmastername = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'activitylogmaster'


class Activitymaster(models.Model):
    activityid = models.SmallIntegerField(primary_key=True)
    trial_activityname_2 = models.CharField(unique=True, max_length=50)
    isfixed = models.BooleanField()
    trial_isactive_4 = models.BooleanField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'activitymaster'


class Addonmaster(models.Model):
    addonid = models.SmallIntegerField(primary_key=True)
    addonname = models.CharField(unique=True, max_length=50)
    rate = models.DecimalField(max_digits=14, decimal_places=3)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    productid = models.CharField(max_length=4)
    revenueledger = models.IntegerField()
    roundingmethod = models.SmallIntegerField()
    roundinglimit = models.DecimalField(max_digits=7, decimal_places=2)
    trial_calculationon_10 = models.SmallIntegerField()
    postingfrequency = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    applydiscount = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'addonmaster'


class Approvaldata(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    trial_approvaldate_5 = models.DateTimeField()
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    remarks = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'approvaldata'


class Attendancedetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Attendanceheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    costcenterid = models.ForeignKey('Costcentermaster', models.DO_NOTHING, db_column='costcenterid')
    trial_attendancetypeid_4 = models.ForeignKey('Attendancetypemaster', models.DO_NOTHING, db_column='trial_attendancetypeid_4')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    trial_period_6 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'attendancedetail'


class Attendanceheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    trial_vchidprefix_3 = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    createlocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_10 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_10')
    trial_recorddatetime_11 = models.DateTimeField()
    sessionid = models.CharField(max_length=6)
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    trial_udffield4_16 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    trial_udffield6_18 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_21 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    trial_auditby_25 = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    trial_datalastchanged_30 = models.BinaryField()
    batchid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'attendanceheader'


class Attendancetypemaster(models.Model):
    attendancetypeid = models.SmallIntegerField(primary_key=True)
    attendancetypename = models.CharField(unique=True, max_length=50)
    trial_period_3 = models.SmallIntegerField()
    type = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'attendancetypemaster'


class Autoimportexport(models.Model):
    trial_mapid_1 = models.ForeignKey('Importexportheader', models.DO_NOTHING, db_column='trial_mapid_1')
    path = models.CharField(max_length=150)
    interval = models.CharField(max_length=50)
    trial_isimport_4 = models.BooleanField()
    trial_stationid_5 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_5')

    class Meta:
        managed = False
        db_table = 'autoimportexport'


class Autoimportsetup(models.Model):
    importfrompath = models.CharField(max_length=500)
    timeinterval = models.CharField(max_length=5)
    moduleid = models.SmallIntegerField()
    trial_mapid_4 = models.SmallIntegerField()
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'autoimportsetup'


class Autonumber(models.Model):
    trial_tableid_1 = models.SmallIntegerField(primary_key=True)
    tablename = models.CharField(max_length=50)
    fieldname = models.CharField(max_length=50)
    lastnumber = models.IntegerField()
    filtercond = models.CharField(max_length=50)
    lastid = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'autonumber'
        unique_together = (('tablename', 'fieldname'),)


class Barcodeprintermaster(models.Model):
    bcprinterid = models.SmallIntegerField(primary_key=True)
    trial_bcprintername_2 = models.CharField(unique=True, max_length=50)
    stationid = models.SmallIntegerField()
    portid = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='portid')
    filename = models.CharField(max_length=500)
    trial_isactive_6 = models.BooleanField()
    isfixed = models.BooleanField()
    trial_mlnumber_8 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'barcodeprintermaster'


class Batchmaster(models.Model):
    batchid = models.CharField(primary_key=True, max_length=6)
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    startdatetime = models.DateTimeField()
    enddatetime = models.DateTimeField()
    trial_dayid_6 = models.ForeignKey('Daymaster', models.DO_NOTHING, db_column='trial_dayid_6')
    daylocationid = models.SmallIntegerField()
    trial_batchidprefix_8 = models.CharField(max_length=15)
    batchidymd = models.CharField(max_length=6)
    newbatchnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'batchmaster'
        unique_together = (('batchid', 'userid', 'locationid'),)


class Brandmaster(models.Model):
    trial_brandid_1 = models.IntegerField(primary_key=True)
    brandname = models.CharField(unique=True, max_length=50)
    principalcompanyid = models.ForeignKey('Principalcompanymaster', models.DO_NOTHING, db_column='principalcompanyid')
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    trial_isfixed_5 = models.BooleanField()
    trial_isactive_6 = models.BooleanField()
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'brandmaster'


class Budgetchild(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_budgetid_2 = models.ForeignKey('Budgetmaster', models.DO_NOTHING, db_column='trial_budgetid_2')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    basis = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'budgetchild'
        unique_together = (('trial_budgetid_2', 'accountid'),)


class Budgetmaster(models.Model):
    trial_budgetid_1 = models.SmallIntegerField(primary_key=True)
    budgetname = models.CharField(unique=True, max_length=50)
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'budgetmaster'


class Cancellationreasonmaster(models.Model):
    cancellationreasonid = models.SmallIntegerField(primary_key=True)
    cancellationreasonname = models.CharField(unique=True, max_length=50)
    trial_reduceinventory_3 = models.BooleanField()
    printonreceipt = models.BooleanField()
    printonkot = models.BooleanField()
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    canceltype = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cancellationreasonmaster'


class Canpolicymaster(models.Model):
    canpolicyid = models.SmallIntegerField(primary_key=True)
    trial_canpolicyname_2 = models.CharField(unique=True, max_length=50)
    beforecheckindays = models.SmallIntegerField()
    chargedays = models.SmallIntegerField()
    chargepercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_chargeamt_6 = models.DecimalField(max_digits=13, decimal_places=3)
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'canpolicymaster'


class Cardtypemaster(models.Model):
    cardtypeid = models.SmallIntegerField(primary_key=True)
    cardtypename = models.CharField(unique=True, max_length=50)
    onsalevalue = models.DecimalField(max_digits=13, decimal_places=3)
    pointawarded = models.DecimalField(max_digits=10, decimal_places=3)
    trial_roundoffid_5 = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='trial_roundoffid_5')
    roundinglimit = models.DecimalField(max_digits=7, decimal_places=2)
    extrapointonbday = models.DecimalField(max_digits=10, decimal_places=3)
    pointtolinkedcustomer = models.DecimalField(max_digits=10, decimal_places=3)
    pointtoconvert = models.DecimalField(max_digits=13, decimal_places=3)
    equivalentcurrency = models.DecimalField(max_digits=13, decimal_places=3)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    trial_margindays_13 = models.SmallIntegerField()
    trial_discountpercent_14 = models.DecimalField(max_digits=6, decimal_places=3)
    calcextrapointmethod = models.SmallIntegerField()
    trial_multiplypointby_16 = models.DecimalField(max_digits=6, decimal_places=3)
    trial_weekdays_17 = models.CharField(max_length=50)
    fromtime = models.DateTimeField()
    totime = models.DateTimeField()
    trial_restrictedsg_20 = models.CharField(max_length=255)
    trial_subscriptiondetail_21 = models.TextField()
    allowdisconsg = models.CharField(max_length=255)
    trial_excludetaxinpoint_23 = models.SmallIntegerField()
    pointawardedonproduct = models.TextField()
    mlnumber = models.BigIntegerField()
    trial_referralpoint_26 = models.DecimalField(max_digits=10, decimal_places=3)
    trial_visitpoint_27 = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'cardtypemaster'


class Cashdrawerbalancing(models.Model):
    srlno = models.BigIntegerField(primary_key=True)
    voucherdate = models.DateTimeField()
    trial_mopid_3 = models.ForeignKey('Modeofpayment', models.DO_NOTHING, db_column='trial_mopid_3')
    trial_userid_4 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_4')
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    trial_sessionid_6 = models.CharField(max_length=6)
    createlocationid = models.SmallIntegerField()
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.SmallIntegerField()
    recorddatetime = models.DateTimeField()
    opening = models.DecimalField(max_digits=18, decimal_places=3)
    trial_closing_12 = models.DecimalField(max_digits=18, decimal_places=3)
    closingdate = models.DateTimeField()
    trial_denominationcl_14 = models.CharField(max_length=4000)
    denominationop = models.CharField(max_length=4000)
    batchid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'cashdrawerbalancing'


class Chargesdetail(models.Model):
    chargesserialnumber = models.BigIntegerField(primary_key=True)
    serialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    trial_chargesid_4 = models.ForeignKey('Chargesmaster', models.DO_NOTHING, db_column='trial_chargesid_4')
    trial_chargestype_5 = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='trial_chargestype_5')
    method = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='method')
    trial_rate_7 = models.DecimalField(max_digits=15, decimal_places=2)
    trial_accountid_8 = models.IntegerField()
    roundingmethod = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='roundingmethod')
    roundinglimit = models.DecimalField(max_digits=7, decimal_places=2)
    trial_chargesamount_11 = models.DecimalField(max_digits=14, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'chargesdetail'
        unique_together = (('serialnumber', 'voucherid', 'trial_chargesid_4'),)


class Chargesmaster(models.Model):
    chargesid = models.SmallIntegerField(primary_key=True)
    trial_chargestype_2 = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='trial_chargestype_2')
    trial_chargesname_3 = models.CharField(unique=True, max_length=50)
    method = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='method')
    rate = models.DecimalField(max_digits=15, decimal_places=2)
    trial_accountid_6 = models.IntegerField()
    roundingmethod = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='roundingmethod')
    roundinglimit = models.DecimalField(max_digits=7, decimal_places=2)
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    addinbill = models.BooleanField()
    addincost = models.BooleanField()
    trial_mlnumber_13 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'chargesmaster'


class Citymaster(models.Model):
    cityid = models.IntegerField(primary_key=True)
    cityname = models.CharField(unique=True, max_length=50)
    trial_stateid_3 = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='trial_stateid_3')
    isactive = models.BooleanField()
    trial_isfixed_5 = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'citymaster'


class Closingstock(models.Model):
    slno = models.IntegerField(primary_key=True)
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    trial_opening_4 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_closingdate_5 = models.DateTimeField()
    closing = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'closingstock'


class Comboproduct(models.Model):
    schemeid = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='schemeid')
    productid = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='productid')
    trial_type_3 = models.SmallIntegerField()
    qty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_andor_5 = models.SmallIntegerField()
    discountpercent = models.DecimalField(max_digits=6, decimal_places=2)
    discountamount = models.DecimalField(max_digits=14, decimal_places=3)
    unitprice = models.DecimalField(max_digits=14, decimal_places=3)
    srlno = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'comboproduct'


class Containerdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_containerserialnumber_2 = models.ForeignKey('Containerheader', models.DO_NOTHING, db_column='trial_containerserialnumber_2')
    containerid = models.ForeignKey('Containermaster', models.DO_NOTHING, db_column='containerid')
    quantity = models.SmallIntegerField()
    trial_weight_5 = models.DecimalField(max_digits=18, decimal_places=4)
    totalweight = models.DecimalField(max_digits=18, decimal_places=4)
    isadd = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'containerdetail'


class Containerheader(models.Model):
    trial_containerserialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    serialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_voucherid_3 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_voucherid_3')
    trial_voucherdate_4 = models.DateTimeField()
    grossweight = models.DecimalField(max_digits=18, decimal_places=4)
    netweight = models.DecimalField(max_digits=18, decimal_places=4)
    trial_tareweight_7 = models.DecimalField(max_digits=18, decimal_places=4)
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    customerid = models.CharField(max_length=5)
    trial_warehouseid_12 = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='trial_warehouseid_12')
    trial_productid_13 = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='trial_productid_13')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'containerheader'


class Containermaster(models.Model):
    containerid = models.SmallIntegerField(primary_key=True)
    containername = models.CharField(max_length=50)
    trial_weight_3 = models.DecimalField(max_digits=18, decimal_places=3)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'containermaster'


class Costcentermaster(models.Model):
    trial_costcenterid_1 = models.IntegerField(primary_key=True)
    trial_costcentername_2 = models.CharField(unique=True, max_length=35)
    isactive = models.BooleanField()
    trial_isfixed_4 = models.BooleanField()
    isemployee = models.BooleanField()
    dateofjoining = models.DateTimeField()
    trial_bloodgroup_7 = models.SmallIntegerField()
    gender = models.SmallIntegerField()
    birthdate = models.DateTimeField()
    trial_fathermothername_10 = models.CharField(max_length=50)
    spouse = models.CharField(max_length=50)
    anniversarydate = models.DateTimeField()
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    address3 = models.CharField(max_length=150)
    cityid = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='cityid')
    stateid = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='stateid')
    pincode = models.CharField(max_length=20)
    trial_countryid_19 = models.ForeignKey('Countrymaster', models.DO_NOTHING, db_column='trial_countryid_19')
    trial_phone_20 = models.CharField(max_length=35)
    trial_mobile_21 = models.CharField(max_length=35)
    trial_email_22 = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    panno = models.CharField(max_length=30)
    pfno = models.CharField(max_length=25)
    trial_esino_26 = models.CharField(max_length=25)
    bankname = models.CharField(max_length=50)
    trial_branchname_28 = models.CharField(max_length=50)
    accountno = models.CharField(max_length=25)
    micrcode = models.CharField(max_length=25)
    trial_picture1_31 = models.CharField(max_length=500)
    picture2 = models.CharField(max_length=500)
    designationid = models.ForeignKey('Matrixlistmaster', models.DO_NOTHING, db_column='designationid')
    departmentid = models.ForeignKey('Matrixlistmaster', models.DO_NOTHING, db_column='departmentid')
    empcode = models.CharField(max_length=16)
    workplanid = models.ForeignKey('Workplanmaster', models.DO_NOTHING, db_column='workplanid')
    trial_fingerscan_37 = models.TextField()
    trial_cardassign_38 = models.BooleanField()
    emfield1 = models.CharField(max_length=50)
    emfield2 = models.CharField(max_length=50)
    emfield3 = models.CharField(max_length=50)
    emfield4 = models.CharField(max_length=50)
    emfield5 = models.CharField(max_length=50)
    trial_emfield6_44 = models.CharField(max_length=50)
    trial_emfield7_45 = models.CharField(max_length=50)
    emfield8 = models.CharField(max_length=50)
    emfield9 = models.CharField(max_length=50)
    emfield10 = models.CharField(max_length=50)
    emptype = models.SmallIntegerField()
    trial_skillids_50 = models.CharField(max_length=50)
    streetnumber = models.CharField(max_length=25)
    streetid = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='streetid')
    trial_localityid_53 = models.ForeignKey('Localitymaster', models.DO_NOTHING, db_column='trial_localityid_53')
    teamid = models.CharField(max_length=50)
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    trial_logsession_57 = models.CharField(max_length=6)
    trial_mlnumber_58 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'costcentermaster'


class Costcentertransaction(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Transactionmaster', models.DO_NOTHING, db_column='serialnumber')
    trial_toby_3 = models.SmallIntegerField()
    trial_accountid_4 = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='trial_accountid_4')
    trial_costcenterid_5 = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='trial_costcenterid_5')
    debitamount = models.DecimalField(max_digits=18, decimal_places=3)
    creditamount = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'costcentertransaction'
        unique_together = (('serialnumber', 'trial_accountid_4', 'trial_costcenterid_5'),)


class Countermaster(models.Model):
    counterid = models.SmallIntegerField(primary_key=True)
    trial_countername_2 = models.CharField(max_length=50)
    trial_isfixed_3 = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'countermaster'


class Countrymaster(models.Model):
    countryid = models.SmallIntegerField(primary_key=True)
    trial_countryname_2 = models.CharField(unique=True, max_length=50)
    decimalsymbol = models.CharField(max_length=1)
    trial_digitafterdecimal_4 = models.SmallIntegerField()
    trial_digitgroupingsymbol_5 = models.CharField(max_length=1)
    digitgroupingformatid = models.SmallIntegerField()
    negativesignsymbol = models.CharField(max_length=1)
    negativeformatid = models.SmallIntegerField()
    displayleadingzero = models.SmallIntegerField()
    trial_dateformatid_10 = models.SmallIntegerField()
    trial_dateseparator_11 = models.CharField(max_length=1)
    timeid = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    trial_weekstartday_15 = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'countrymaster'


class Crmpointredeemdata(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    customerid = models.CharField(max_length=5)
    crmpoints = models.DecimalField(max_digits=13, decimal_places=3)
    module = models.SmallIntegerField()
    trial_ssrserialnumber_6 = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'crmpointredeemdata'


class Currencymaster(models.Model):
    currencyid = models.SmallIntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    trial_formalname_3 = models.CharField(max_length=20)
    trial_positiveformatid_4 = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='trial_positiveformatid_4')
    trial_negativeformatid_5 = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='trial_negativeformatid_5')
    decimalsymbol = models.CharField(max_length=1)
    trial_digitafterdecimal_7 = models.SmallIntegerField()
    symbolfordecimalportion = models.CharField(max_length=15)
    digitgroupingsymbol = models.CharField(max_length=1)
    digitgroupingformatid = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='digitgroupingformatid')
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    amtinwordtype = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'currencymaster'
        unique_together = (('symbol', 'trial_formalname_3', 'symbolfordecimalportion'),)


class Customerfeedback(models.Model):
    trial_feedbackid_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    customerid = models.CharField(max_length=5)
    typeid = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='typeid')
    productid = models.CharField(max_length=4)
    remarks = models.CharField(max_length=500)
    trial_voucherdate_6 = models.DateTimeField()
    field1 = models.CharField(max_length=500)
    field2 = models.CharField(max_length=500)
    field3 = models.CharField(max_length=500)
    trial_field4_10 = models.CharField(max_length=500)
    field5 = models.CharField(max_length=500)
    trial_field6_12 = models.CharField(max_length=500)
    trial_field7_13 = models.CharField(max_length=500)
    trial_field8_14 = models.CharField(max_length=500)
    trial_field9_15 = models.CharField(max_length=500)
    trial_field10_16 = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'customerfeedback'


class Customerinout(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    customerid = models.CharField(max_length=5)
    trial_datetimein_3 = models.DateTimeField()
    datetimeout = models.DateTimeField()
    noofguest = models.SmallIntegerField()
    nameofguest = models.CharField(max_length=50)
    trial_remarks_7 = models.CharField(max_length=500)
    trial_sessionidin_8 = models.CharField(max_length=6)
    sessionidout = models.CharField(max_length=6)
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    useridin = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='useridin')
    trial_useridout_12 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_useridout_12')

    class Meta:
        managed = False
        db_table = 'customerinout'


class Customerpointredeem(models.Model):
    redeemid = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    trial_customerid_3 = models.CharField(max_length=5)
    method = models.ForeignKey('Formatmaster', models.DO_NOTHING, db_column='method')
    point = models.DecimalField(max_digits=13, decimal_places=3)
    createlocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='createlocationid')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    remarks = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customerpointredeem'


class Customertypemaster(models.Model):
    customertypeid = models.SmallIntegerField(primary_key=True)
    customertypename = models.CharField(unique=True, max_length=50)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'customertypemaster'


class Dailyattendance(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    createlocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    trial_sessionid_5 = models.CharField(max_length=6)
    costcenterid = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='costcenterid')
    trial_scandatetime_7 = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dailyattendance'


class Dataretrieve(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    tableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='tableid')
    trial_fieldid_3 = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='trial_fieldid_3')
    returnfield = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='returnfield')
    joinfield = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='joinfield')

    class Meta:
        managed = False
        db_table = 'dataretrieve'
        unique_together = (('tableid', 'trial_fieldid_3', 'returnfield'),)


class Datasendchild(models.Model):
    datasendid = models.ForeignKey('Datasendmaster', models.DO_NOTHING, db_column='datasendid')
    dataid = models.SmallIntegerField()
    trial_locationid_3 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_locationid_3')
    trial_syncdata_4 = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'datasendchild'


class Datasendmaster(models.Model):
    datasendid = models.SmallIntegerField(primary_key=True)
    datasendname = models.CharField(unique=True, max_length=50)
    trial_isfixed_3 = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasendmaster'


class Datatypemaster(models.Model):
    datatypeid = models.SmallIntegerField(primary_key=True)
    trial_datatypename_2 = models.CharField(unique=True, max_length=100)
    datatypeformat = models.CharField(max_length=20)
    display = models.CharField(max_length=15)
    trial_prefixsuffix_5 = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'datatypemaster'


class Daymaster(models.Model):
    dayid = models.CharField(primary_key=True, max_length=6)
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    trial_startdatetime_3 = models.DateTimeField()
    enddatetime = models.DateTimeField()
    openuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='openuserid')
    closeuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='closeuserid')

    class Meta:
        managed = False
        db_table = 'daymaster'
        unique_together = (('dayid', 'locationid'),)


class Departmentmaster(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    departmentname = models.CharField(unique=True, max_length=50)
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    isactive = models.BooleanField()
    trial_isfixed_5 = models.BooleanField()
    trial_mlnumber_6 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'departmentmaster'


class Dependantmaster(models.Model):
    trial_serialnumber_1 = models.IntegerField(primary_key=True)
    tableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='tableid')
    dependanttableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='dependanttableid')
    dependantfieldid = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='dependantfieldid')

    class Meta:
        managed = False
        db_table = 'dependantmaster'
        unique_together = (('tableid', 'dependanttableid', 'dependantfieldid'),)


class Designationcategory(models.Model):
    trial_categoryid_1 = models.SmallIntegerField(primary_key=True)
    trial_categoryname_2 = models.CharField(max_length=25)
    defaultweight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designationcategory'


class Designationchild(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    designationid = models.ForeignKey('Designationmaster', models.DO_NOTHING, db_column='designationid')
    applicationid = models.IntegerField()
    applicationweight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designationchild'


class Designationmaster(models.Model):
    designationid = models.SmallIntegerField(primary_key=True)
    designationname = models.CharField(unique=True, max_length=50)
    trial_backdays_3 = models.SmallIntegerField()
    postdays = models.SmallIntegerField()
    discountpercent = models.DecimalField(max_digits=13, decimal_places=3)
    discountvalue = models.DecimalField(max_digits=13, decimal_places=3)
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    trial_loginplusday_9 = models.SmallIntegerField()
    loginminusday = models.SmallIntegerField()
    logincontrolplus = models.SmallIntegerField()
    logincontrolminus = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()
    trial_stopdatasynchr_17 = models.SmallIntegerField()
    warningdatasynchr = models.SmallIntegerField()
    backdtentryafterdayclose = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'designationmaster'


class Discountcouponchild(models.Model):
    couponid = models.CharField(primary_key=True, max_length=20)
    trial_discountcouponid_2 = models.ForeignKey('Discountcouponmaster', models.DO_NOTHING, db_column='trial_discountcouponid_2')
    trial_redeemed_3 = models.IntegerField()
    userid = models.SmallIntegerField()
    trial_createdate_5 = models.DateTimeField()
    issuedate = models.DateTimeField()
    trial_customerid_7 = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'discountcouponchild'


class Discountcouponmaster(models.Model):
    discountcouponid = models.SmallIntegerField(primary_key=True)
    discountcouponname = models.CharField(unique=True, max_length=50)
    printname = models.CharField(max_length=50)
    schemeid = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='schemeid')
    locationids = models.CharField(max_length=2048)
    maxredeem = models.SmallIntegerField()
    restrictedmop = models.CharField(max_length=150)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'discountcouponmaster'


class Displaymaster(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    tableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='tableid')
    fieldid = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='fieldid')
    trial_parentfieldid_4 = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='trial_parentfieldid_4')
    parenttableid = models.IntegerField()
    parentjoinfieldid = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='parentjoinfieldid')
    joinfieldid = models.ForeignKey('Fieldmaster', models.DO_NOTHING, db_column='joinfieldid')
    displayorder = models.DecimalField(max_digits=8, decimal_places=2)
    datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='datatypeid')
    caption = models.CharField(max_length=50)
    trial_compulsoryfield_11 = models.SmallIntegerField()
    displaylist = models.SmallIntegerField()
    colwidth = models.SmallIntegerField()
    trial_jointype_14 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'displaymaster'
        unique_together = (('tableid', 'fieldid'),)


class Driverinout(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_createlocationid_2 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_createlocationid_2')
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    datetimein = models.DateTimeField()
    datetimeout = models.DateTimeField()
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    vehicleid = models.ForeignKey('Vehiclemaster', models.DO_NOTHING, db_column='vehicleid')
    startingmeter = models.IntegerField()
    endingmeter = models.IntegerField()
    inuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='inuserid')
    trial_outuserid_12 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_outuserid_12')
    insessionid = models.CharField(max_length=6)
    trial_recorddatetime_14 = models.DateTimeField()
    instationid = models.SmallIntegerField()
    trial_datalastchanged_16 = models.BinaryField()
    outsessionid = models.CharField(max_length=6)
    outstationid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'driverinout'


class Electionmaster(models.Model):
    electionid = models.SmallIntegerField(primary_key=True)
    electionname = models.CharField(unique=True, max_length=50)
    electionstartdatetime = models.DateTimeField()
    trial_electionenddatetime_4 = models.DateTimeField()
    trial_nominationstartdatetime_5 = models.DateTimeField()
    trial_nominationenddatetime_6 = models.DateTimeField()
    agefrom = models.SmallIntegerField()
    ageto = models.SmallIntegerField()
    trial_checkdues_9 = models.BooleanField()
    trial_checkduesdate_10 = models.DateTimeField()
    checkduesvalidation = models.SmallIntegerField()
    cardissuedateupto = models.DateTimeField()
    checkcardexpirydate = models.BooleanField()
    trial_expirygracedays_14 = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'electionmaster'


class Electionmembertype(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    electionid = models.ForeignKey(Electionmaster, models.DO_NOTHING, db_column='electionid')
    membertype = models.ForeignKey(Customertypemaster, models.DO_NOTHING, db_column='membertype')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'electionmembertype'
        unique_together = (('electionid', 'membertype'),)


class Electionpostmaster(models.Model):
    trial_srlno_1 = models.SmallIntegerField(primary_key=True)
    trial_electionid_2 = models.ForeignKey(Electionmaster, models.DO_NOTHING, db_column='trial_electionid_2')
    postid = models.ForeignKey('Postmaster', models.DO_NOTHING, db_column='postid')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'electionpostmaster'
        unique_together = (('trial_electionid_2', 'postid'),)


class Employeeschedule(models.Model):
    trial_costcenterid_1 = models.OneToOneField(Costcentermaster, models.DO_NOTHING, db_column='trial_costcenterid_1', primary_key=True)
    schdate = models.DateTimeField()
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    trial_workplanid_4 = models.ForeignKey('Workplanmaster', models.DO_NOTHING, db_column='trial_workplanid_4')
    trial_saletarget_5 = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'employeeschedule'
        unique_together = (('trial_costcenterid_1', 'schdate'),)


class Feedbackdata(models.Model):
    trial_feedbackid_1 = models.ForeignKey('Feedbackmaster', models.DO_NOTHING, db_column='trial_feedbackid_1')
    scale1 = models.SmallIntegerField()
    scale2 = models.SmallIntegerField()
    scale3 = models.SmallIntegerField()
    scale4 = models.SmallIntegerField()
    scale5 = models.SmallIntegerField()
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    tablename = models.CharField(max_length=15)
    customerid = models.CharField(max_length=5)
    feedbackdatetime = models.DateTimeField()
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    trial_saleserialnumber_15 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_createlocationid_16 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_createlocationid_16')
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'feedbackdata'


class Feedbackmaster(models.Model):
    feedbackid = models.SmallIntegerField(primary_key=True)
    trial_feedbackname_2 = models.CharField(unique=True, max_length=50)
    feedbackdescription = models.CharField(max_length=500)
    trial_scaletype_4 = models.SmallIntegerField()
    scale1 = models.CharField(max_length=500)
    scale2 = models.CharField(max_length=500)
    scale3 = models.CharField(max_length=500)
    scale4 = models.CharField(max_length=500)
    scale5 = models.CharField(max_length=500)
    question1 = models.CharField(max_length=500)
    question2 = models.CharField(max_length=500)
    question3 = models.CharField(max_length=500)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'feedbackmaster'


class Festivalmaster(models.Model):
    trial_festivalid_1 = models.SmallIntegerField(primary_key=True)
    festivalname = models.CharField(max_length=50)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'festivalmaster'


class Fieldmaster(models.Model):
    serialnumber = models.IntegerField()
    trial_fieldid_2 = models.IntegerField(primary_key=True)
    fieldname = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    tableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='tableid')
    datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='datatypeid')
    minlength = models.SmallIntegerField()
    trial_maxlength_8 = models.SmallIntegerField()
    trial_originalfieldid_9 = models.IntegerField()
    trial_noofline_10 = models.SmallIntegerField()
    trial_filter_11 = models.CharField(max_length=512)
    convertpropercase = models.SmallIntegerField()
    type = models.SmallIntegerField()
    trial_updateatbranch_14 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fieldmaster'


class Forcedquestionchild(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    forcedquestionid = models.ForeignKey('Forcedquestionmaster', models.DO_NOTHING, db_column='forcedquestionid')
    productid = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='productid')
    rate = models.DecimalField(max_digits=14, decimal_places=3)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    thirdpartyjson = models.TextField()

    class Meta:
        managed = False
        db_table = 'forcedquestionchild'
        unique_together = (('forcedquestionid', 'productid'),)


class Forcedquestionmaster(models.Model):
    forcedquestionid = models.SmallIntegerField(primary_key=True)
    trial_forcedquestionname_2 = models.CharField(unique=True, max_length=50)
    enforceanswer = models.BooleanField()
    noofchoice = models.SmallIntegerField()
    isactive = models.BooleanField()
    trial_isfixed_6 = models.BooleanField()
    trial_loguser_7 = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()
    thirdpartyjson = models.TextField()

    class Meta:
        managed = False
        db_table = 'forcedquestionmaster'


class Foreigndbtable(models.Model):
    trial_application_1 = models.CharField(max_length=50)
    connectionstring = models.CharField(max_length=255)
    queryget = models.CharField(max_length=4000)
    trial_queryset_4 = models.CharField(max_length=4000)
    allowsave = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'foreigndbtable'


class Formatmaster(models.Model):
    formatid = models.SmallIntegerField(primary_key=True)
    formattype = models.CharField(max_length=50)
    vbprefix = models.CharField(max_length=50)
    vbsuffix = models.CharField(max_length=50)
    trial_sqlprefix_5 = models.CharField(max_length=50)
    sqlsuffix = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'formatmaster'


class Giftvoucherchild(models.Model):
    gvcode = models.CharField(primary_key=True, max_length=20)
    giftvoucherid = models.ForeignKey('Giftvouchermaster', models.DO_NOTHING, db_column='giftvoucherid')
    redeemed = models.SmallIntegerField()
    redeemamt = models.DecimalField(max_digits=14, decimal_places=3)
    userid = models.SmallIntegerField()
    createdate = models.DateTimeField()
    trial_productid_7 = models.CharField(max_length=4)
    trial_childid_8 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=14, decimal_places=3)
    serialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    isactive = models.BooleanField()
    issuedate = models.DateTimeField()
    customerid = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'giftvoucherchild'


class Giftvouchermaster(models.Model):
    giftvoucherid = models.SmallIntegerField(primary_key=True)
    giftvouchername = models.CharField(unique=True, max_length=50)
    printname = models.CharField(max_length=50)
    trial_validtilldate_4 = models.DateTimeField()
    locationids = models.CharField(max_length=2048)
    voucheramount = models.DecimalField(max_digits=14, decimal_places=3)
    maxredeem = models.IntegerField()
    trial_productid_8 = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='trial_productid_8')
    stockjournalvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='stockjournalvoucherid')
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()
    trial_validitydays_13 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'giftvouchermaster'


class Groupmaster(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(unique=True, max_length=50)
    parentgroupid = models.IntegerField()
    grouptypeid = models.ForeignKey('Grouptypemaster', models.DO_NOTHING, db_column='grouptypeid')
    trial_isactive_5 = models.BooleanField()
    isfixed = models.BooleanField()
    trial_mlnumber_7 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'groupmaster'


class Grouptypemaster(models.Model):
    grouptypeid = models.SmallIntegerField(primary_key=True)
    trial_grouptypename_2 = models.CharField(unique=True, max_length=30)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'grouptypemaster'


class Gstruploaddata(models.Model):
    srlno = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    transactionid = models.CharField(max_length=50)
    trial_finperiod_4 = models.CharField(max_length=10)
    trial_json_5 = models.TextField()
    response = models.TextField()
    trial_gstinno_7 = models.CharField(max_length=20)
    responseackno = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gstruploaddata'


class Holidaymaster(models.Model):
    trial_srlno_1 = models.SmallIntegerField(primary_key=True)
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    year = models.SmallIntegerField()
    holidayname = models.CharField(max_length=50)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    trial_mlnumber_7 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'holidaymaster'


class Hoteltransactiondata(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    reservationid = models.CharField(max_length=15)
    voucherdate = models.DateTimeField()
    amount = models.DecimalField(max_digits=14, decimal_places=3)
    isadd = models.BooleanField()
    remarks = models.TextField()
    transactiontype = models.SmallIntegerField()
    transactionserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_billedto_9 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'hoteltransactiondata'


class Hsnsacmaster(models.Model):
    hsnsacid = models.IntegerField(primary_key=True)
    hsnsaccode = models.CharField(unique=True, max_length=20)
    hsnsacname = models.CharField(max_length=50)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()
    uqc = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'hsnsacmaster'


class Importexportdetail(models.Model):
    mapid = models.ForeignKey('Importexportheader', models.DO_NOTHING, db_column='mapid')
    colpos = models.IntegerField()
    fieldid = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='fieldid')
    relatedto = models.CharField(max_length=50)
    filetype = models.CharField(max_length=50)
    includeheader = models.BooleanField()
    totalcols = models.IntegerField()
    isimport = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'importexportdetail'
        unique_together = (('mapid', 'fieldid'),)


class Importexportheader(models.Model):
    trial_mapid_1 = models.IntegerField(primary_key=True)
    mapname = models.CharField(unique=True, max_length=50)
    mapfolder = models.CharField(max_length=300)
    mapfile = models.CharField(max_length=100)
    trial_moduleid_5 = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'importexportheader'


class Inboxdata(models.Model):
    trial_id_1 = models.DecimalField(unique=True, max_digits=18, decimal_places=4)
    trial_inboxxml_2 = models.TextField()
    isinserted = models.BooleanField()
    trial_date_4 = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inboxdata'


class Ipbxsetting(models.Model):
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    vendorid = models.SmallIntegerField()
    stationdata = models.TextField()
    trial_isactive_4 = models.BooleanField()
    othersetting = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ipbxsetting'
        unique_together = (('locationid', 'vendorid'),)


class Issuecustdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Issuecustheader', models.DO_NOTHING, db_column='serialnumber')
    productid = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='productid')
    trial_childid_4 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    remarks = models.CharField(max_length=255)
    tracknumber = models.CharField(max_length=15)
    trial_jobid_10 = models.ForeignKey('Jobmaster', models.DO_NOTHING, db_column='trial_jobid_10')
    recdserialnumber = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'issuecustdetail'


class Issuecustheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.SmallIntegerField()
    customerid = models.CharField(max_length=5)
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='createlocationid')
    trial_locationid_10 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_locationid_10')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_12 = models.SmallIntegerField()
    trial_recorddatetime_13 = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    recdserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_udffield1_16 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    trial_isaudited_27 = models.BooleanField()
    auditby = models.SmallIntegerField()
    trial_auditdate_29 = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'issuecustheader'


class Issuejobberdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Issuejobberheader', models.DO_NOTHING, db_column='serialnumber')
    trial_productid_3 = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='trial_productid_3')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    remarks = models.CharField(max_length=255)
    trial_tracknumber_9 = models.CharField(max_length=15)
    trial_jobid_10 = models.ForeignKey('Jobmaster', models.DO_NOTHING, db_column='trial_jobid_10')

    class Meta:
        managed = False
        db_table = 'issuejobberdetail'


class Issuejobberheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.SmallIntegerField()
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='createlocationid')
    trial_locationid_10 = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='trial_locationid_10')
    modifylocationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='modifylocationid')
    userid = models.SmallIntegerField()
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    udffield1 = models.CharField(max_length=50)
    trial_udffield2_16 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    trial_udffield4_18 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_24 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    trial_datalastchanged_32 = models.BinaryField()
    trial_batchid_33 = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'issuejobberheader'


class Jobmaster(models.Model):
    jobid = models.SmallIntegerField(primary_key=True)
    jobname = models.CharField(unique=True, max_length=50)
    jobdays = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'jobmaster'


class Jointable(models.Model):
    trial_tablenamefrom_1 = models.CharField(primary_key=True, max_length=6)
    tablenameto = models.CharField(max_length=6)
    joinedon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jointable'
        unique_together = (('trial_tablenamefrom_1', 'tablenameto'),)


class Languagemaster(models.Model):
    languageid = models.SmallIntegerField(primary_key=True)
    trial_languagename_2 = models.CharField(max_length=50)
    languagecode = models.CharField(max_length=5)
    languagedata = models.TextField()

    class Meta:
        managed = False
        db_table = 'languagemaster'


class Layoutchild(models.Model):
    layoutid = models.ForeignKey('Layoutmaster', models.DO_NOTHING, db_column='layoutid')
    trial_position_2 = models.SmallIntegerField()
    tablename = models.CharField(max_length=6)
    tablestatus = models.SmallIntegerField()
    alias = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'layoutchild'
        unique_together = (('layoutid', 'trial_position_2', 'tablename'),)


class Layoutmaster(models.Model):
    layoutid = models.SmallIntegerField(primary_key=True)
    trial_layoutname_2 = models.CharField(unique=True, max_length=20)
    trial_isactive_3 = models.BooleanField()
    trial_isfixed_4 = models.BooleanField()
    teamid = models.CharField(max_length=50)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'layoutmaster'


class Listeditorchild(models.Model):
    trial_srlno_1 = models.SmallIntegerField(primary_key=True)
    listid = models.ForeignKey('Listeditormaster', models.DO_NOTHING, db_column='listid')
    fieldid = models.ForeignKey('Listeditorfieldmaster', models.DO_NOTHING, db_column='fieldid')
    width = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'listeditorchild'


class Listeditorfieldmaster(models.Model):
    trial_fieldid_1 = models.SmallIntegerField(primary_key=True)
    trial_fieldname_2 = models.CharField(max_length=25)
    trial_queryfield_3 = models.CharField(max_length=255, blank=True, null=True)
    defaultwidth = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'listeditorfieldmaster'
        unique_together = (('trial_fieldname_2', 'trial_queryfield_3'),)


class Listeditormaster(models.Model):
    trial_listid_1 = models.SmallIntegerField(primary_key=True)
    listname = models.CharField(unique=True, max_length=50)
    trial_displaywidth_3 = models.SmallIntegerField()
    trial_fieldfilter_4 = models.CharField(max_length=255, blank=True, null=True)
    defaultfield = models.CharField(max_length=255)
    tablename = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'listeditormaster'


class Listmaster(models.Model):
    listid = models.SmallIntegerField(primary_key=True)
    trial_listname_2 = models.CharField(unique=True, max_length=35)
    isfixed = models.BooleanField()
    trial_isactive_4 = models.BooleanField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'listmaster'


class Listtemp(models.Model):
    trial_mainid_1 = models.IntegerField(blank=True, null=True)
    trial_parentid_2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listtemp'


class Localitymaster(models.Model):
    localityid = models.IntegerField(primary_key=True)
    localityname = models.CharField(unique=True, max_length=50)
    trial_cityid_3 = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='trial_cityid_3')
    trial_stateid_4 = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='trial_stateid_4')
    countryid = models.ForeignKey(Countrymaster, models.DO_NOTHING, db_column='countryid')
    locationid = models.SmallIntegerField()
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    minbillamt = models.DecimalField(max_digits=14, decimal_places=3)
    deliverycharge = models.DecimalField(max_digits=14, decimal_places=3)
    distance = models.IntegerField()
    estimatedtime = models.IntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'localitymaster'


class Locationemailsetup(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    locationid = models.ForeignKey('Locationmaster', models.DO_NOTHING, db_column='locationid')
    trial_reporttype_3 = models.SmallIntegerField()
    trial_sendto_4 = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    trial_attachmenttype_6 = models.SmallIntegerField()
    trial_dataperiod_7 = models.SmallIntegerField()
    frequency = models.SmallIntegerField()
    trial_sendtime_9 = models.DateTimeField()
    body = models.TextField()
    isactive = models.BooleanField()
    isalert = models.SmallIntegerField()
    formatfile = models.CharField(max_length=500)
    sendtomodify = models.CharField(max_length=500)
    trial_locationids_15 = models.CharField(max_length=500)
    mlnumber = models.BigIntegerField()
    stationid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'locationemailsetup'


class Locationexportsetting(models.Model):
    locationid = models.OneToOneField('Locationmaster', models.DO_NOTHING, db_column='locationid', primary_key=True)
    trial_createfileondayclose_2 = models.SmallIntegerField()
    countrycode = models.CharField(max_length=50)
    interfaceid = models.CharField(max_length=50)
    interfacename = models.CharField(max_length=50)
    unitid = models.CharField(max_length=50)
    currencycode = models.CharField(max_length=50)
    trial_exportfolder_8 = models.CharField(max_length=500)
    trial_tenantid_9 = models.CharField(max_length=50)
    trial_createfileondayclosetp1_10 = models.SmallIntegerField()
    createfileondayclosesun = models.SmallIntegerField()
    trial_companycode_12 = models.CharField(max_length=50)
    cashjournalcode = models.CharField(max_length=50)
    businessarea = models.CharField(max_length=50)
    costcenter = models.CharField(max_length=50)
    trial_businessplace_16 = models.CharField(max_length=50)
    sectioncode = models.CharField(max_length=50)
    createfileondayclosecashsheet = models.SmallIntegerField()
    createfileondayclosenoncashsheet = models.SmallIntegerField()
    trial_profitcenter_20 = models.CharField(max_length=50)
    mlnumber = models.BigIntegerField()
    createfileondayclosegst = models.SmallIntegerField()
    createfileondayclosesergentmajor = models.SmallIntegerField()
    excludemopinsap = models.CharField(max_length=50)
    trial_plantcode_25 = models.CharField(max_length=50)
    purchaseorganization = models.CharField(max_length=50)
    locationsprpg = models.CharField(max_length=100)
    trial_createfileondayclosepr_28 = models.SmallIntegerField()
    createfileondayclosepg = models.SmallIntegerField()
    cashsheetgroup = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'locationexportsetting'


class Locationmaster(models.Model):
    trial_locationid_1 = models.SmallIntegerField(primary_key=True)
    locationname = models.CharField(unique=True, max_length=100)
    trial_companyname_3 = models.CharField(max_length=75)
    locationcode = models.CharField(unique=True, max_length=3)
    currencyid = models.ForeignKey(Currencymaster, models.DO_NOTHING, db_column='currencyid')
    trial_regionid_6 = models.ForeignKey(Countrymaster, models.DO_NOTHING, db_column='trial_regionid_6')
    financialyear = models.DateTimeField()
    trial_bookbegin_8 = models.DateTimeField()
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    address3 = models.CharField(max_length=150)
    cityid = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='cityid')
    stateid = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='stateid')
    trial_region_14 = models.CharField(max_length=50)
    countryid = models.ForeignKey(Countrymaster, models.DO_NOTHING, db_column='countryid')
    pincode = models.CharField(max_length=20)
    trial_phone_17 = models.CharField(max_length=35)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    panno = models.CharField(max_length=30)
    cstno = models.CharField(max_length=30)
    trial_vatno_23 = models.CharField(max_length=30)
    servicetaxno = models.CharField(max_length=30)
    trial_isactive_25 = models.BooleanField()
    setlinkinformation = models.BooleanField()
    mathodoflink = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='mathodoflink')
    timeinterval = models.CharField(max_length=5)
    trial_datasendid_29 = models.SmallIntegerField()
    emailaddress = models.CharField(max_length=50)
    emailpassword = models.CharField(max_length=50)
    trial_usessl_32 = models.BooleanField()
    trial_incomingmailserver_33 = models.CharField(max_length=50)
    incomingserverport = models.IntegerField()
    outgoingmailserver = models.CharField(max_length=50)
    outgoingserverport = models.IntegerField()
    trial_outgoingauthentication_37 = models.BooleanField()
    trial_exportfolder_38 = models.CharField(max_length=255)
    importfolder = models.CharField(max_length=255)
    trial_isfixed_40 = models.BooleanField()
    autobackup = models.SmallIntegerField()
    incrementalbackup = models.BooleanField()
    trial_backupfolder_43 = models.CharField(max_length=500)
    trial_target_44 = models.DecimalField(max_digits=14, decimal_places=2)
    area = models.IntegerField()
    staff = models.IntegerField()
    activatescheme = models.BooleanField()
    activatesms = models.BooleanField()
    trial_smshost_49 = models.CharField(max_length=500)
    trial_createmldata_50 = models.BooleanField()
    lmfield1 = models.CharField(max_length=50)
    lmfield2 = models.CharField(max_length=50)
    trial_lmfield3_53 = models.CharField(max_length=50)
    trial_lmfield4_54 = models.CharField(max_length=50)
    lmfield5 = models.CharField(max_length=50)
    lmfield6 = models.CharField(max_length=50)
    lmfield7 = models.CharField(max_length=50)
    trial_lmfield8_58 = models.CharField(max_length=50)
    trial_lmfield9_59 = models.CharField(max_length=50)
    lmfield10 = models.CharField(max_length=50)
    trial_iplastrecd_61 = models.DateTimeField()
    trial_iplastsend_62 = models.DateTimeField()
    checkintime = models.CharField(max_length=5)
    checkouttime = models.CharField(max_length=5)
    trial_nightaudittime_65 = models.CharField(max_length=5)
    todaynightauditon = models.SmallIntegerField()
    enforcenightaudit = models.SmallIntegerField()
    trial_highweekdays_68 = models.CharField(max_length=50)
    pendingdata = models.IntegerField()
    masterdata = models.TextField()
    recdbatchsize = models.SmallIntegerField()
    trial_generatetask_72 = models.SmallIntegerField()
    workplanid = models.ForeignKey('Workplanmaster', models.DO_NOTHING, db_column='workplanid')
    streetnumber = models.CharField(max_length=25)
    streetid = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='streetid')
    trial_localityid_76 = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='trial_localityid_76')
    checkout24 = models.SmallIntegerField()
    earlycheckinpolicy = models.CharField(max_length=500)
    earlycheckoutpolicy = models.CharField(max_length=500)
    latecheckoutpolicy = models.CharField(max_length=500)
    iscallcenter = models.SmallIntegerField()
    allowdayopenclose = models.SmallIntegerField()
    showcp = models.SmallIntegerField()
    timeintervalforspa = models.SmallIntegerField()
    trial_kotstartingnumber_85 = models.IntegerField()
    trial_kotprefix_86 = models.CharField(max_length=10)
    kotnumbersystemid = models.SmallIntegerField()
    teamid = models.CharField(max_length=50)
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    trial_logsession_91 = models.CharField(max_length=6)
    trial_otherdb_92 = models.CharField(max_length=4000)
    gpslatitude = models.DecimalField(max_digits=18, decimal_places=6)
    gpslongitude = models.DecimalField(max_digits=18, decimal_places=6)
    weblogo = models.CharField(max_length=50)
    mindeliveryamt = models.DecimalField(max_digits=10, decimal_places=3)
    freedeliveryabove = models.DecimalField(max_digits=10, decimal_places=3)
    trial_deliverycharges_98 = models.DecimalField(max_digits=10, decimal_places=3)
    opentime = models.CharField(max_length=10)
    trial_closetime_100 = models.CharField(max_length=10)
    webmenuid = models.SmallIntegerField()
    allowpickup = models.SmallIntegerField()
    allowhd = models.SmallIntegerField()
    allowtablereservation = models.SmallIntegerField()
    allowdinein = models.SmallIntegerField()
    trial_allowmenuview_106 = models.SmallIntegerField()
    weblocationname = models.CharField(max_length=100)
    apiport = models.CharField(max_length=4)
    trial_webmenu_109 = models.TextField()
    mlnumber = models.BigIntegerField()
    trial_timeintervalsyncmaster_111 = models.CharField(max_length=5)
    databaseversion = models.DecimalField(max_digits=10, decimal_places=4)
    trial_gstinno_113 = models.CharField(max_length=20)
    batchstartingnumber = models.IntegerField()
    batchprefix = models.CharField(max_length=10)
    trial_batchnumbersystemid_116 = models.SmallIntegerField()
    trial_gstreturnsetting_117 = models.TextField()
    trial_autoscheduletime_118 = models.CharField(max_length=5)
    dayduration = models.IntegerField()
    physicalstockprocess = models.SmallIntegerField()
    autostkjrnlondayclose = models.SmallIntegerField()
    trial_mobilenolength_122 = models.SmallIntegerField()
    trial_scaledbsetup_123 = models.TextField()
    createoutbox = models.BooleanField()
    multipleprintexe = models.SmallIntegerField()
    thirdpartyjson = models.TextField()
    contravoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='contravoucherid')
    debitnotevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='debitnotevoucherid')
    creditnotevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='creditnotevoucherid')
    journalvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='journalvoucherid')
    trial_paymentvoucherid_131 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_paymentvoucherid_131')
    trial_receiptvoucherid_132 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_receiptvoucherid_132')
    trial_accopeningvoucherid_133 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_accopeningvoucherid_133')
    physicalstockvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='physicalstockvoucherid')
    stockjournalvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='stockjournalvoucherid')
    trial_purchasevoucherid_136 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_purchasevoucherid_136')
    purchasereturnvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='purchasereturnvoucherid')
    salevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='salevoucherid')
    salereturnvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='salereturnvoucherid')
    stocktransfervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='stocktransfervoucherid')
    trial_stocktransferordervoucherid_141 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_stocktransferordervoucherid_141')
    openingstockvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='openingstockvoucherid')
    saleordervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='saleordervoucherid')
    purchaseordervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='purchaseordervoucherid')
    trial_receivefromcustomerid_145 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_receivefromcustomerid_145')
    issuetojobberid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='issuetojobberid')
    receivefromjobberid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='receivefromjobberid')
    issuetocustomerid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='issuetocustomerid')
    purchasechallanid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='purchasechallanid')
    rejectionoutid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='rejectionoutid')
    salechallanid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='salechallanid')
    rejectioninid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='rejectioninid')
    ratechangeid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='ratechangeid')
    prepaidid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='prepaidid')
    trial_payrollvoucherid_155 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_payrollvoucherid_155')
    attendancevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='attendancevoucherid')
    roomreservationvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='roomreservationvoucherid')
    workordervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='workordervoucherid')

    class Meta:
        managed = False
        db_table = 'locationmaster'


class Locationprocesssetup(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    trial_locationid_2 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_2')
    reporttype = models.SmallIntegerField()
    dataperiod = models.SmallIntegerField()
    trial_frequency_5 = models.SmallIntegerField()
    trial_sendtime_6 = models.DateTimeField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()
    trial_stationid_9 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'locationprocesssetup'


class Locationsmssetup(models.Model):
    trial_srlno_1 = models.SmallIntegerField(primary_key=True)
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    trial_reporttype_3 = models.SmallIntegerField()
    trial_sendto_4 = models.CharField(max_length=500)
    dataperiod = models.SmallIntegerField()
    frequency = models.SmallIntegerField()
    sendtime = models.DateTimeField()
    body = models.TextField()
    isactive = models.BooleanField()
    isalert = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()
    stationid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'locationsmssetup'


class Locationtaxmaster(models.Model):
    srlno = models.IntegerField(primary_key=True)
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    producttaxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='producttaxid')
    locationtaxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='locationtaxid')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'locationtaxmaster'


class Locationvendormaster(models.Model):
    trial_locationid_1 = models.OneToOneField(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_1', primary_key=True)
    vendorid = models.SmallIntegerField()
    url = models.CharField(max_length=500)
    retailerid = models.CharField(max_length=50)
    trial_outletid_5 = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isqsr = models.SmallIntegerField()
    userid = models.SmallIntegerField()
    trial_mopid_9 = models.SmallIntegerField()
    responseurl = models.CharField(max_length=500)
    vendorjson = models.TextField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'locationvendormaster'
        unique_together = (('trial_locationid_1', 'vendorid'),)


class Mastercreation(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    tableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='tableid')
    fieldid = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='fieldid')
    trial_displayorder_4 = models.DecimalField(max_digits=6, decimal_places=3)
    trial_storefield_5 = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='trial_storefield_5')
    trial_movecursor_6 = models.SmallIntegerField()
    list = models.SmallIntegerField()
    checkduplicate = models.SmallIntegerField()
    conditionid = models.SmallIntegerField()
    joinfield = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='joinfield')
    defaultvalue = models.CharField(max_length=50)
    copydatafrom = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='copydatafrom')
    isprimary = models.SmallIntegerField()
    signbeforeinput = models.CharField(max_length=1)
    insertupdate = models.SmallIntegerField()
    trial_rowheading_16 = models.CharField(max_length=50)
    singlemultiplerow = models.SmallIntegerField()
    masterfield = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mastercreation'
        unique_together = (('tableid', 'fieldid', 'trial_displayorder_4'),)


class Matrixlistmaster(models.Model):
    dataid = models.IntegerField(primary_key=True)
    trial_dataname_2 = models.CharField(max_length=50)
    listid = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='listid')
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    trial_displayorder_6 = models.SmallIntegerField()
    trial_mlnumber_7 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'matrixlistmaster'
        unique_together = (('trial_dataname_2', 'listid'),)


class Matrixmaster(models.Model):
    matrixid = models.SmallIntegerField(primary_key=True)
    trial_matrixname_2 = models.CharField(unique=True, max_length=50)
    field1name = models.CharField(max_length=35)
    trial_field1listid_4 = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='trial_field1listid_4')
    field2name = models.CharField(max_length=35)
    trial_field2listid_6 = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='trial_field2listid_6')
    field3name = models.CharField(max_length=35)
    field3listid = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='field3listid')
    trial_field4name_9 = models.CharField(max_length=35)
    field4datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field4datatypeid')
    field5name = models.CharField(max_length=35)
    field5datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field5datatypeid')
    field6name = models.CharField(max_length=35)
    field6datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field6datatypeid')
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    linkfieldname = models.CharField(max_length=35)
    activateexpiry = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'matrixmaster'


class Menuchild(models.Model):
    trial_serialnumber_1 = models.IntegerField(primary_key=True)
    trial_parentmenuid_2 = models.IntegerField()
    menuid = models.IntegerField()
    childmenuid = models.IntegerField()
    formname = models.CharField(max_length=50)
    formtag = models.CharField(max_length=255)
    menucaption = models.CharField(max_length=50)
    movecursor = models.SmallIntegerField()
    displayorder = models.DecimalField(max_digits=6, decimal_places=3)
    shortcutkey = models.CharField(max_length=10)
    rowheading = models.CharField(max_length=50)
    query = models.CharField(max_length=255)
    trial_imagename_13 = models.BinaryField()
    applicationid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'menuchild'
        unique_together = (('trial_serialnumber_1', 'trial_parentmenuid_2', 'menuid', 'childmenuid'), ('trial_parentmenuid_2', 'childmenuid', 'menuid'),)


class Menumaster(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    menuid = models.IntegerField(unique=True)
    menuname = models.CharField(max_length=50)
    menucaption = models.CharField(max_length=50)
    trial_grouping_5 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'menumaster'


class Modeofpayment(models.Model):
    mopid = models.SmallIntegerField(primary_key=True)
    mopname = models.CharField(unique=True, max_length=50)
    trial_moptypeid_3 = models.ForeignKey('Modeofpaymenttype', models.DO_NOTHING, db_column='trial_moptypeid_3')
    accountid = models.IntegerField()
    customerinfo = models.BooleanField()
    documentnumber = models.BooleanField()
    bankname = models.BooleanField()
    crmpoints = models.BooleanField()
    directtender = models.BooleanField()
    istipallowed = models.BooleanField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    exchangerate = models.DecimalField(max_digits=23, decimal_places=10)
    vendorid = models.SmallIntegerField()
    commissionpercent = models.DecimalField(max_digits=7, decimal_places=3)
    commissionledger = models.IntegerField()
    trial_validitydays_17 = models.SmallIntegerField()
    otpreqdforcrm = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    trial_logsession_21 = models.CharField(max_length=6)
    vendorinputtype = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()
    shortcutkey = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'modeofpayment'


class Modeofpaymentchild(models.Model):
    trial_serialnumber_1 = models.IntegerField(primary_key=True)
    mopid = models.SmallIntegerField()
    denominationname = models.CharField(max_length=25)
    trial_denominationvalue_4 = models.DecimalField(max_digits=13, decimal_places=3)
    trial_denominationpicture_5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'modeofpaymentchild'


class Modeofpaymenttype(models.Model):
    moptypeid = models.SmallIntegerField(primary_key=True)
    moptypename = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'modeofpaymenttype'


class Nominationmaster(models.Model):
    trial_nominationid_1 = models.SmallIntegerField(primary_key=True)
    trial_electionid_2 = models.ForeignKey(Electionmaster, models.DO_NOTHING, db_column='trial_electionid_2')
    postid = models.ForeignKey('Postmaster', models.DO_NOTHING, db_column='postid')
    contestant = models.CharField(max_length=5)
    trial_isfixed_5 = models.BooleanField()
    applieddate = models.DateTimeField()
    trial_isactive_7 = models.BooleanField()
    party = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'nominationmaster'
        unique_together = (('trial_electionid_2', 'postid', 'contestant'),)


class Noshowpolicymaster(models.Model):
    noshowpolicyid = models.SmallIntegerField(primary_key=True)
    trial_noshowpolicyname_2 = models.CharField(unique=True, max_length=50)
    aftercheckinhrs = models.SmallIntegerField()
    chargedays = models.SmallIntegerField()
    chargepercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargeamt = models.DecimalField(max_digits=13, decimal_places=3)
    trial_isfixed_7 = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'noshowpolicymaster'


class Openotherwindow(models.Model):
    trial_serialnumber_1 = models.IntegerField(primary_key=True)
    trial_tableid_2 = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='trial_tableid_2')
    fieldid = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='fieldid')
    condition = models.CharField(max_length=25)
    opentableid = models.ForeignKey('Tablemaster', models.DO_NOTHING, db_column='opentableid')
    singlemultiplerow = models.SmallIntegerField()
    trial_formname_7 = models.CharField(max_length=25)
    trial_displaycontent_8 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'openotherwindow'


class Oposmaster(models.Model):
    oposid = models.SmallIntegerField(primary_key=True)
    trial_oposname_2 = models.CharField(unique=True, max_length=50)
    opostype = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='opostype')
    trial_pnoofcols_4 = models.SmallIntegerField()
    numberofcopy = models.SmallIntegerField()
    trial_pnooflinesafterprint_6 = models.SmallIntegerField()
    pcutpaperafterprint = models.BooleanField()
    trial_printlogo_8 = models.BooleanField()
    trial_logofile_9 = models.CharField(max_length=255)
    lddisplaymode = models.SmallIntegerField()
    ldblinkrate = models.SmallIntegerField()
    ldnoofline = models.SmallIntegerField()
    ldnoofcharacter = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    drivertype = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='drivertype')
    trial_deviceport_17 = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='trial_deviceport_17')
    noofcolscondense = models.SmallIntegerField()
    condensenormal = models.CharField(max_length=25)
    condensebold = models.CharField(max_length=25)
    trial_standardnormal_21 = models.CharField(max_length=25)
    standardbold = models.CharField(max_length=25)
    trial_dblwidthnormal_23 = models.CharField(max_length=25)
    dblwidthbold = models.CharField(max_length=25)
    centeralign = models.CharField(max_length=25)
    leftalign = models.CharField(max_length=25)
    cutcommand = models.CharField(max_length=25)
    cashdrawercommand = models.CharField(max_length=25)
    printformat = models.SmallIntegerField()
    trial_barcodecommand_30 = models.CharField(max_length=25)
    customerdisplayfile = models.CharField(max_length=255)
    pnooflinesbeforeprint = models.SmallIntegerField()
    trial_buzzercommand_33 = models.CharField(max_length=25)
    opendrawer = models.SmallIntegerField()
    htmlcssstyle = models.TextField()
    trial_mlnumber_36 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oposmaster'


class Optionchild(models.Model):
    optionid = models.ForeignKey('Optionmaster', models.DO_NOTHING, db_column='optionid')
    optiontypeid = models.ForeignKey('Optiontypemaster', models.DO_NOTHING, db_column='optiontypeid')
    trial_optiondata_3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'optionchild'
        unique_together = (('optionid', 'optiontypeid'),)


class Optionmaster(models.Model):
    trial_optionid_1 = models.SmallIntegerField(primary_key=True)
    optionname = models.CharField(unique=True, max_length=100)
    optiontypeid = models.ForeignKey('Optiontypemaster', models.DO_NOTHING, db_column='optiontypeid')
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'optionmaster'


class Optiontypemaster(models.Model):
    trial_optiontypeid_1 = models.SmallIntegerField(primary_key=True)
    optiontypename = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'optiontypemaster'


class Outboxdata(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    outboxxml = models.TextField()
    trial_locationid_3 = models.SmallIntegerField()
    isuploaded = models.BooleanField()
    trial_date_5 = models.DateTimeField()
    isresponse = models.SmallIntegerField()
    priority = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'outboxdata'


class Payheadcalcformula(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    payheadid = models.ForeignKey('Payheadmaster', models.DO_NOTHING, db_column='payheadid')
    trial_payheadchildid_3 = models.ForeignKey('Payheadmaster', models.DO_NOTHING, db_column='trial_payheadchildid_3')
    trial_addless_4 = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'payheadcalcformula'


class Payheadmaster(models.Model):
    trial_payheadid_1 = models.SmallIntegerField(primary_key=True)
    payheadname = models.CharField(unique=True, max_length=50)
    trial_printname_3 = models.CharField(max_length=50)
    payheadtype = models.SmallIntegerField()
    affectnetsalary = models.BooleanField()
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    calctype = models.SmallIntegerField()
    attendancetypeid = models.ForeignKey(Attendancetypemaster, models.DO_NOTHING, db_column='attendancetypeid')
    trial_calcperiod_9 = models.SmallIntegerField()
    daysasper = models.SmallIntegerField()
    daysinperiod = models.SmallIntegerField()
    trial_calcformula_12 = models.SmallIntegerField()
    isfixed = models.BooleanField()
    trial_isactive_14 = models.BooleanField()
    displayorder = models.SmallIntegerField()
    trial_mlnumber_16 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'payheadmaster'


class Payheadrange(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    payheadid = models.ForeignKey(Payheadmaster, models.DO_NOTHING, db_column='payheadid')
    trial_startdate_3 = models.DateTimeField()
    trial_fromamount_4 = models.DecimalField(max_digits=13, decimal_places=4)
    toamount = models.DecimalField(max_digits=13, decimal_places=4)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    value = models.DecimalField(max_digits=13, decimal_places=4)
    trial_mlnumber_8 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'payheadrange'


class Physicalstockdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Physicalstockheader', models.DO_NOTHING, db_column='serialnumber')
    productid = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='productid')
    trial_childid_4 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    trial_purchasecost_8 = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    pcostamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    srateamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    trial_conversionfactor_14 = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'physicalstockdetail'


class Physicalstockheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    trial_vchidprefix_3 = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    trial_compareid_8 = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='trial_compareid_8')
    trial_createlocationid_9 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_9')
    trial_locationid_10 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_10')
    trial_modifylocationid_11 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_modifylocationid_11')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    trial_narration_14 = models.CharField(max_length=255)
    sessionid = models.CharField(max_length=6)
    pcosttotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_qtytotal_17 = models.DecimalField(max_digits=18, decimal_places=4)
    sratetotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_udffield1_19 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    trial_udffield5_23 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    trial_udffield7_25 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_28 = models.CharField(max_length=50)
    trial_stationid_29 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_29')
    isaudited = models.BooleanField()
    trial_auditby_31 = models.SmallIntegerField()
    trial_auditdate_32 = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    trial_link_35 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'physicalstockheader'


class Postmaster(models.Model):
    postid = models.SmallIntegerField(primary_key=True)
    postname = models.CharField(unique=True, max_length=50)
    trial_noofpost_3 = models.SmallIntegerField()
    noofselection = models.SmallIntegerField()
    agefrom = models.SmallIntegerField()
    trial_ageto_6 = models.SmallIntegerField()
    checkdues = models.BooleanField()
    trial_checkduesdate_8 = models.DateTimeField()
    checkduesvalidation = models.SmallIntegerField()
    trial_cardissuedateupto_10 = models.DateTimeField()
    checkcardexpirydate = models.BooleanField()
    expirygracedays = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'postmaster'


class Postmembertype(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    postid = models.ForeignKey(Postmaster, models.DO_NOTHING, db_column='postid')
    trial_membertype_3 = models.ForeignKey(Customertypemaster, models.DO_NOTHING, db_column='trial_membertype_3')
    trial_mlnumber_4 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'postmembertype'
        unique_together = (('postid', 'trial_membertype_3'),)


class Prepaidtransaction(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    customerid = models.CharField(max_length=5)
    trial_cardserial_3 = models.IntegerField()
    trial_voucherdate_4 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_6 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    trial_voucherid_8 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_voucherid_8')
    transactiontype = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='transactiontype')
    mopid = models.ForeignKey(Modeofpayment, models.DO_NOTHING, db_column='mopid')
    amount = models.DecimalField(max_digits=18, decimal_places=3)
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_16 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_16')
    recorddatetime = models.DateTimeField()
    accountserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    exchangerate = models.DecimalField(max_digits=23, decimal_places=10)
    stationid = models.SmallIntegerField()
    batchid = models.CharField(max_length=6)
    documentno = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    trial_response_24 = models.TextField()

    class Meta:
        managed = False
        db_table = 'prepaidtransaction'


class Pricelistchild(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    pricelistid = models.ForeignKey('Pricelistmaster', models.DO_NOTHING, db_column='pricelistid')
    productid = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='productid')
    rate = models.DecimalField(max_digits=14, decimal_places=3)
    discpercent = models.DecimalField(max_digits=5, decimal_places=2)
    discamt = models.DecimalField(max_digits=14, decimal_places=3)
    markup = models.DecimalField(max_digits=6, decimal_places=2)
    trial_margin_8 = models.DecimalField(max_digits=6, decimal_places=2)
    taxid = models.SmallIntegerField()
    trial_pluspercent_10 = models.DecimalField(max_digits=6, decimal_places=2)
    minuspercent = models.DecimalField(max_digits=6, decimal_places=2)
    rateunitid = models.SmallIntegerField()
    brandid = models.ForeignKey(Brandmaster, models.DO_NOTHING, db_column='brandid')
    subgroupid = models.ForeignKey('Subgroupmaster', models.DO_NOTHING, db_column='subgroupid')
    pricecap = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'pricelistchild'
        unique_together = (('pricelistid', 'productid', 'brandid', 'subgroupid'),)


class Pricelistlocation(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    pricelistid = models.ForeignKey('Pricelistmaster', models.DO_NOTHING, db_column='pricelistid')
    trial_locationid_3 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_3')

    class Meta:
        managed = False
        db_table = 'pricelistlocation'
        unique_together = (('pricelistid', 'trial_locationid_3'),)


class Pricelistmaster(models.Model):
    pricelistid = models.SmallIntegerField(primary_key=True)
    pricelistname = models.CharField(unique=True, max_length=50)
    trial_type_3 = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='trial_type_3')
    trial_isactive_4 = models.BooleanField()
    isfixed = models.BooleanField()
    trial_teamid_6 = models.CharField(max_length=50)
    pricingon = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    trial_loglocation_9 = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pricelistmaster'


class Principalcompanymaster(models.Model):
    principalcompanyid = models.IntegerField(primary_key=True)
    principalcompanyname = models.CharField(unique=True, max_length=50)
    trial_isactive_3 = models.BooleanField()
    trial_isfixed_4 = models.BooleanField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'principalcompanymaster'


class Printerredirectmaster(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    trial_stationid_2 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_2')
    trial_oposid_3 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='trial_oposid_3')
    trial_redirectstationid_4 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_redirectstationid_4')
    redirectoposid = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='redirectoposid')

    class Meta:
        managed = False
        db_table = 'printerredirectmaster'
        unique_together = (('trial_stationid_2', 'trial_oposid_3'),)


class Productchildmaster(models.Model):
    productid = models.ForeignKey('Productmaster', models.DO_NOTHING, db_column='productid')
    trial_childid_2 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    trial_productchildid_4 = models.CharField(primary_key=True, max_length=11)
    trial_purchaserate_5 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_minuspercent_6 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_pluspercent_7 = models.DecimalField(max_digits=6, decimal_places=2)
    purchasecost = models.DecimalField(max_digits=14, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    markup = models.DecimalField(max_digits=15, decimal_places=2)
    margin = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.DecimalField(max_digits=15, decimal_places=2)
    trial_sellingprice_13 = models.DecimalField(max_digits=14, decimal_places=3)
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    trial_matrixlistid1_15 = models.ForeignKey(Matrixlistmaster, models.DO_NOTHING, db_column='trial_matrixlistid1_15')
    matrixlistid2 = models.ForeignKey(Matrixlistmaster, models.DO_NOTHING, db_column='matrixlistid2')
    trial_matrixlistid3_17 = models.ForeignKey(Matrixlistmaster, models.DO_NOTHING, db_column='trial_matrixlistid3_17')
    trial_field1_18 = models.CharField(max_length=50)
    field2 = models.CharField(max_length=50)
    trial_field3_20 = models.CharField(max_length=50)
    matrixid = models.SmallIntegerField()
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_spcommamt_23 = models.DecimalField(max_digits=14, decimal_places=3)
    schemeids = models.CharField(max_length=250)
    schemedisc = models.DecimalField(max_digits=15, decimal_places=2)
    trial_link_26 = models.CharField(max_length=512)
    mfgdate = models.DateTimeField()
    best = models.SmallIntegerField()
    before = models.SmallIntegerField()
    expdate = models.DateTimeField()
    trial_creationdate_31 = models.DateTimeField()
    recorddatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'productchildmaster'
        unique_together = (('productid', 'trial_childid_2', 'locationcode'),)


class Productgroupmaster(models.Model):
    trial_productgroupid_1 = models.IntegerField(primary_key=True)
    productgroupname = models.CharField(unique=True, max_length=50)
    departmentid = models.ForeignKey(Departmentmaster, models.DO_NOTHING, db_column='departmentid')
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    trial_isactive_5 = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'productgroupmaster'


class Productmaster(models.Model):
    trial_productid_1 = models.CharField(primary_key=True, max_length=4)
    productname = models.CharField(unique=True, max_length=50, blank=True, null=True)
    printname = models.CharField(max_length=50, blank=True, null=True)
    upcean = models.CharField(unique=True, max_length=20)
    trial_userdefinedcode_5 = models.CharField(max_length=16)
    trial_maxretailprice_6 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_brandid_7 = models.ForeignKey(Brandmaster, models.DO_NOTHING, db_column='trial_brandid_7')
    subgroupid = models.ForeignKey('Subgroupmaster', models.DO_NOTHING, db_column='subgroupid')
    productgroupid = models.ForeignKey(Productgroupmaster, models.DO_NOTHING, db_column='productgroupid')
    departmentid = models.ForeignKey(Departmentmaster, models.DO_NOTHING, db_column='departmentid')
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    trial_binlocation_12 = models.CharField(max_length=10)
    trial_matrixid_13 = models.ForeignKey(Matrixmaster, models.DO_NOTHING, db_column='trial_matrixid_13')
    evalcount = models.IntegerField()
    taxidpurchase = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidpurchase')
    taxidsale = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidsale')
    trial_printbarcode_17 = models.BooleanField()
    askrate = models.BooleanField()
    trial_usefifo_19 = models.BooleanField()
    productmessage = models.CharField(max_length=255)
    quantityonhand = models.DecimalField(max_digits=13, decimal_places=3)
    trial_reorderinformation_22 = models.BooleanField()
    reorderlevel = models.DecimalField(max_digits=13, decimal_places=3)
    trial_safetylevel_24 = models.DecimalField(max_digits=13, decimal_places=3)
    reorderquantity = models.DecimalField(max_digits=13, decimal_places=3)
    minimumorderquantity = models.DecimalField(max_digits=13, decimal_places=3)
    standardsaleprice = models.DecimalField(max_digits=14, decimal_places=3)
    trial_standardcostprice_28 = models.DecimalField(max_digits=14, decimal_places=3)
    productdiscount = models.DecimalField(max_digits=5, decimal_places=2)
    trial_allowoperatordiscount_30 = models.BooleanField()
    productremarks = models.CharField(max_length=255)
    picture1 = models.CharField(max_length=500)
    picture2 = models.CharField(max_length=500)
    trial_recipecomponents_34 = models.BooleanField()
    trial_recorddatetime_35 = models.DateTimeField()
    companyid = models.SmallIntegerField()
    trial_sessionid_37 = models.CharField(max_length=6)
    trial_isactive_38 = models.BooleanField()
    isfixed = models.BooleanField()
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.SmallIntegerField()
    trial_changeconversion_42 = models.BooleanField()
    itemtype = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='itemtype')
    weighingscaleexport = models.BooleanField()
    trial_weighingscaleconversion_45 = models.IntegerField()
    trial_printnameother_46 = models.CharField(max_length=35)
    trial_generateproductchild_47 = models.SmallIntegerField()
    trial_couponfile_48 = models.CharField(max_length=500)
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    schemeids = models.CharField(max_length=250)
    trial_pmfield1_52 = models.CharField(max_length=50)
    pmfield2 = models.CharField(max_length=50)
    trial_pmfield3_54 = models.CharField(max_length=50)
    pmfield4 = models.CharField(max_length=50)
    trial_pmfield5_56 = models.CharField(max_length=50)
    pmfield6 = models.CharField(max_length=50)
    trial_pmfield7_58 = models.CharField(max_length=50)
    pmfield8 = models.CharField(max_length=50)
    pmfield9 = models.CharField(max_length=50)
    pmfield10 = models.CharField(max_length=50)
    calcnetweight = models.BooleanField()
    barcoderatio = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=512)
    askquantity = models.SmallIntegerField()
    askcontainer = models.SmallIntegerField()
    serviceitem = models.CharField(max_length=4)
    rate = models.DecimalField(max_digits=14, decimal_places=3)
    periodicity = models.SmallIntegerField()
    upcean1 = models.CharField(unique=True, max_length=20)
    upcean2 = models.CharField(unique=True, max_length=20)
    trial_upcean3_72 = models.CharField(unique=True, max_length=20)
    upcean4 = models.CharField(unique=True, max_length=20)
    trial_teamid_74 = models.CharField(max_length=50)
    trial_changecontainerweight_75 = models.SmallIntegerField()
    trial_saleaccountid_76 = models.IntegerField()
    salereturnaccountid = models.IntegerField()
    trial_purchaseaccountid_78 = models.IntegerField()
    purchasereturnaccountid = models.IntegerField()
    taxablevalue = models.DecimalField(max_digits=14, decimal_places=3)
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    webgroupid = models.SmallIntegerField()
    websubgroupid = models.SmallIntegerField()
    webitemname = models.CharField(max_length=500)
    trial_isrecommended_87 = models.SmallIntegerField()
    foodtype = models.SmallIntegerField()
    spicelevel = models.SmallIntegerField()
    webproductname = models.CharField(max_length=50)
    convertproductid = models.CharField(max_length=4)
    convertqty = models.DecimalField(max_digits=13, decimal_places=3)
    mlnumber = models.BigIntegerField()
    hsnsacid = models.ForeignKey(Hsnsacmaster, models.DO_NOTHING, db_column='hsnsacid')
    productcodesap = models.CharField(max_length=50)
    generateproduction = models.SmallIntegerField()
    trial_spcommdatewise_97 = models.CharField(max_length=1000)
    sacid = models.ForeignKey(Hsnsacmaster, models.DO_NOTHING, db_column='sacid')

    class Meta:
        managed = False
        db_table = 'productmaster'


class Productmatrixrelationmaster(models.Model):
    srlno = models.IntegerField(primary_key=True)
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    dataid = models.ForeignKey(Matrixlistmaster, models.DO_NOTHING, db_column='dataid')
    trial_listid_4 = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='trial_listid_4')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'productmatrixrelationmaster'


class Productrecipemaster(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    recipeproductid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='recipeproductid')
    recipequantity = models.DecimalField(max_digits=13, decimal_places=3)
    isfixed = models.BooleanField()
    trial_isactive_7 = models.BooleanField()
    remarks = models.CharField(max_length=4000)
    overhead = models.DecimalField(max_digits=13, decimal_places=3)
    factor = models.DecimalField(max_digits=13, decimal_places=3)
    trial_productset_11 = models.SmallIntegerField()
    issemi = models.BooleanField()
    trial_calccoston_13 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'productrecipemaster'
        unique_together = (('productid', 'recipeproductid'),)


class Productroqmaster(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    roqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_rono_6 = models.SmallIntegerField()
    roperiod = models.SmallIntegerField()
    rotype = models.SmallIntegerField()
    trial_roround_9 = models.SmallIntegerField()
    moqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_mono_11 = models.SmallIntegerField()
    moperiod = models.SmallIntegerField()
    motype = models.SmallIntegerField()
    trial_moround_14 = models.SmallIntegerField()
    trial_mlnumber_15 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'productroqmaster'
        unique_together = (('locationid', 'warehouseid', 'productid'),)


class Properties(models.Model):
    serialnumber = models.IntegerField()
    id = models.SmallIntegerField(primary_key=True)
    propertyname = models.CharField(unique=True, max_length=50)
    trial_propertydatatype_4 = models.SmallIntegerField()
    trial_weight_5 = models.IntegerField()
    propertycaption = models.CharField(max_length=50)
    trial_propertycolor_7 = models.IntegerField()
    trial_otherinfo_8 = models.CharField(max_length=255)
    isinputatpurchase = models.SmallIntegerField()
    trial_checkatsales_10 = models.SmallIntegerField()
    evaluatechange = models.SmallIntegerField()
    propdefvalue = models.CharField(max_length=10)
    displayatsales = models.SmallIntegerField()
    propertyorder = models.SmallIntegerField()
    columnwidth = models.SmallIntegerField()
    companyid = models.SmallIntegerField()
    trial_sessionid_17 = models.CharField(max_length=6)
    isdeleted = models.BooleanField()
    trial_propertyinternalcaption_19 = models.CharField(max_length=255)
    trial_flatfieldname_20 = models.CharField(max_length=50)
    savevalue = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'properties'


class Purchasechallandetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Purchasechallanheader', models.DO_NOTHING, db_column='serialnumber')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=18, decimal_places=3)
    sellingrate = models.DecimalField(max_digits=18, decimal_places=3)
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=13, decimal_places=3)
    trial_taxamount_13 = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    trial_taxrate1_16 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount2_20 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    trial_taxrate3_22 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_itemvalue_27 = models.DecimalField(max_digits=32, decimal_places=6, blank=True, null=True)
    trial_isdeleted_28 = models.BooleanField()
    poserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_discpercent_30 = models.DecimalField(max_digits=8, decimal_places=2)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_alternateunitid_32 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_alternateunitid_32')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    trial_inputrate_35 = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    chargespercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_discountpercent_40 = models.DecimalField(max_digits=5, decimal_places=2)
    discountamount = models.DecimalField(max_digits=14, decimal_places=3)
    pur = models.DecimalField(max_digits=13, decimal_places=3)
    trial_pr_43 = models.DecimalField(max_digits=13, decimal_places=3)
    cr = models.DecimalField(max_digits=13, decimal_places=3)
    bal = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    grouprow = models.IntegerField()
    calcmethod = models.SmallIntegerField()
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue4_51 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'purchasechallandetail'


class Purchasechallanheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    supplierref = models.CharField(max_length=30)
    supplierrefdate = models.DateTimeField()
    duedate = models.DateTimeField()
    margin = models.DecimalField(max_digits=6, decimal_places=2)
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    narration = models.CharField(max_length=255)
    trial_sessionid_15 = models.CharField(max_length=6)
    isdeleted = models.BooleanField()
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    trial_modifylocationid_19 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_modifylocationid_19')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    taxtotal = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    trial_udffield1_26 = models.CharField(max_length=50)
    trial_udffield2_27 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    trial_udffield4_29 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_34 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    trial_stationid_36 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_36')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    trial_auditdate_39 = models.DateTimeField()
    trial_auditlocation_40 = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_placeofsupply_45 = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='trial_placeofsupply_45')

    class Meta:
        managed = False
        db_table = 'purchasechallanheader'


class Purchasechallanreturndetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Purchasechallanreturnheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=14, decimal_places=3)
    trial_sellingrate_9 = models.DecimalField(max_digits=14, decimal_places=3)
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    trial_taxid_11 = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='trial_taxid_11')
    taxrate = models.DecimalField(max_digits=13, decimal_places=3)
    trial_taxamount_13 = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount1_17 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxid2_18 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount3_23 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    trial_taxrate4_25 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    itemvalue = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    isdeleted = models.BooleanField()
    trial_pcserialnumber_29 = models.DecimalField(max_digits=18, decimal_places=4)
    discpercent = models.DecimalField(max_digits=8, decimal_places=2)
    trial_alternateqty_31 = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    trial_conversionfactor_33 = models.DecimalField(max_digits=13, decimal_places=3)
    trial_unitid_34 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_unitid_34')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    trial_inputrateperqty_37 = models.DecimalField(max_digits=13, decimal_places=3)
    chargespercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    discountpercent = models.DecimalField(max_digits=5, decimal_places=2)
    discountamount = models.DecimalField(max_digits=14, decimal_places=3)
    calcmethod = models.SmallIntegerField()
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue4 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'purchasechallanreturndetail'


class Purchasechallanreturnheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    supplierref = models.CharField(max_length=30)
    supplierrefdate = models.DateTimeField()
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    narration = models.CharField(max_length=255)
    trial_sessionid_13 = models.CharField(max_length=6)
    isdeleted = models.BooleanField()
    trial_createlocationid_15 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_15')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_18 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_18')
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    taxtotal = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    udffield1 = models.CharField(max_length=50)
    trial_udffield2_25 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_32 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    trial_isaudited_35 = models.BooleanField()
    trial_auditby_36 = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    trial_link_40 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    trial_batchid_42 = models.CharField(max_length=6)
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')

    class Meta:
        managed = False
        db_table = 'purchasechallanreturnheader'


class Purchasedetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Purchaseheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    trial_childid_4 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    trial_quantity_7 = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=18, decimal_places=3)
    trial_sellingrate_9 = models.DecimalField(max_digits=18, decimal_places=3)
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=13, decimal_places=3)
    trial_taxamount_13 = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    trial_taxid1_15 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxid2_18 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    itemvalue = models.DecimalField(max_digits=32, decimal_places=6, blank=True, null=True)
    trial_isdeleted_28 = models.BooleanField()
    poserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    discpercent = models.DecimalField(max_digits=8, decimal_places=2)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_alternateunitid_32 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_alternateunitid_32')
    trial_conversionfactor_33 = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    trial_inputrateunitid_36 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_inputrateunitid_36')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_pcserialnumber_38 = models.DecimalField(max_digits=18, decimal_places=4)
    chargespercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    discountpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_discountamount_42 = models.DecimalField(max_digits=14, decimal_places=3)
    grouprow = models.IntegerField()
    calcmethod = models.SmallIntegerField()
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue2_46 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue4_48 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'purchasedetail'


class Purchaseheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    supplierref = models.CharField(max_length=30)
    trial_supplierrefdate_9 = models.DateTimeField()
    duedate = models.DateTimeField()
    margin = models.DecimalField(max_digits=6, decimal_places=2)
    poserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    trial_narration_15 = models.CharField(max_length=255)
    trial_purchaseaccountid_16 = models.IntegerField()
    trial_sessionid_17 = models.CharField(max_length=6)
    isdeleted = models.BooleanField()
    trial_createlocationid_19 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_19')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_accountserialnumber_22 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_userid_23 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_23')
    recorddatetime = models.DateTimeField()
    isopening = models.BooleanField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_taxtotal_28 = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    trial_udffield8_37 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    trial_isaudited_41 = models.BooleanField()
    auditby = models.SmallIntegerField()
    trial_auditdate_43 = models.DateTimeField()
    trial_auditlocation_44 = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_placeofsupply_49 = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='trial_placeofsupply_49')

    class Meta:
        managed = False
        db_table = 'purchaseheader'


class Purchaseorderdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Purchaseorderheader', models.DO_NOTHING, db_column='serialnumber')
    trial_productid_3 = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='trial_productid_3')
    trial_childid_4 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    trial_productchildid_6 = models.CharField(max_length=11)
    trial_quantity_7 = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=14, decimal_places=3)
    sellingrate = models.DecimalField(max_digits=14, decimal_places=3)
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=13, decimal_places=3)
    taxamount = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxid2_18 = models.IntegerField()
    trial_taxrate2_19 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount4_26 = models.DecimalField(max_digits=18, decimal_places=3)
    itemvalue = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    trial_isdeleted_28 = models.BooleanField()
    pur = models.DecimalField(max_digits=13, decimal_places=3)
    pr = models.DecimalField(max_digits=13, decimal_places=3)
    trial_discpercent_31 = models.DecimalField(max_digits=8, decimal_places=2)
    trial_alternateqty_32 = models.DecimalField(max_digits=13, decimal_places=3)
    trial_alternateunitid_33 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_alternateunitid_33')
    trial_conversionfactor_34 = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    trial_inputrate_36 = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    adj = models.DecimalField(max_digits=13, decimal_places=3)
    purch = models.DecimalField(max_digits=13, decimal_places=3)
    prch = models.DecimalField(max_digits=13, decimal_places=3)
    bal = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    chargespercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    discountpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_discountamount_46 = models.DecimalField(max_digits=14, decimal_places=3)
    grouprow = models.IntegerField()
    calcmethod = models.SmallIntegerField()
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue2_50 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue4_52 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'purchaseorderdetail'


class Purchaseorderheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    trial_vchidprefix_3 = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    supplierref = models.CharField(max_length=30)
    supplierrefdate = models.DateTimeField()
    trial_duedate_10 = models.DateTimeField()
    trial_margin_11 = models.DecimalField(max_digits=6, decimal_places=2)
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    narration = models.CharField(max_length=255)
    purchaseaccountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='purchaseaccountid')
    trial_sessionid_16 = models.CharField(max_length=6)
    isdeleted = models.BooleanField()
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    trial_locationid_19 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_19')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    accountserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_userid_22 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_22')
    recorddatetime = models.DateTimeField()
    isopening = models.BooleanField()
    trial_qtytotal_25 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_subtotal_26 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_taxtotal_27 = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    trial_udffield4_32 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    trial_udffield6_34 = models.CharField(max_length=50)
    trial_udffield7_35 = models.CharField(max_length=50)
    trial_udffield8_36 = models.CharField(max_length=50)
    trial_udffield9_37 = models.CharField(max_length=50)
    trial_udffield10_38 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    trial_auditlocation_43 = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    trial_link_45 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    trial_batchid_47 = models.CharField(max_length=6)
    trial_approvalno_48 = models.SmallIntegerField()
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')

    class Meta:
        managed = False
        db_table = 'purchaseorderheader'


class Purchasereturndetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Purchasereturnheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    trial_childid_4 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    trial_productchildid_6 = models.CharField(max_length=11)
    trial_quantity_7 = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=14, decimal_places=3)
    sellingrate = models.DecimalField(max_digits=14, decimal_places=3)
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    trial_taxid_11 = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='trial_taxid_11')
    trial_taxrate_12 = models.DecimalField(max_digits=13, decimal_places=3)
    taxamount = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    trial_taxid1_15 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    itemvalue = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    isdeleted = models.BooleanField()
    poserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_discpercent_30 = models.DecimalField(max_digits=8, decimal_places=2)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    trial_inputrateunitid_36 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_inputrateunitid_36')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_chargespercent_38 = models.DecimalField(max_digits=5, decimal_places=2)
    trial_chargesamount_39 = models.DecimalField(max_digits=14, decimal_places=3)
    discountpercent = models.DecimalField(max_digits=5, decimal_places=2)
    discountamount = models.DecimalField(max_digits=14, decimal_places=3)
    calcmethod = models.SmallIntegerField()
    trial_taxablevalue1_43 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue4 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'purchasereturndetail'


class Purchasereturnheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    trial_accountid_7 = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='trial_accountid_7')
    trial_supplierref_8 = models.CharField(max_length=30)
    trial_supplierrefdate_9 = models.DateTimeField()
    trial_purchaseserialnumber_10 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_poserialnumber_11 = models.DecimalField(max_digits=18, decimal_places=4)
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    narration = models.CharField(max_length=255)
    purchaseaccountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='purchaseaccountid')
    sessionid = models.CharField(max_length=6)
    trial_isdeleted_17 = models.BooleanField()
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    accountserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    trial_qtytotal_24 = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    taxtotal = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_36 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    trial_stationid_38 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_38')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    trial_auditremarks_43 = models.CharField(max_length=255)
    trial_link_44 = models.CharField(max_length=512)
    trial_datalastchanged_45 = models.BinaryField()
    trial_batchid_46 = models.CharField(max_length=6)
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')
    purchasebillno = models.CharField(max_length=20)
    trial_purchasebilldate_49 = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchasereturnheader'


class Ratecardchild(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    ratecardid = models.ForeignKey('Ratecardmaster', models.DO_NOTHING, db_column='ratecardid')
    roomtypeid = models.ForeignKey('Roomtypemaster', models.DO_NOTHING, db_column='roomtypeid')
    trial_lwbaserate_4 = models.DecimalField(max_digits=14, decimal_places=3)
    lwrateextra = models.DecimalField(max_digits=14, decimal_places=3)
    lwrateextrabed = models.DecimalField(max_digits=14, decimal_places=3)
    hwbaserate = models.DecimalField(max_digits=14, decimal_places=3)
    hwrateextra = models.DecimalField(max_digits=14, decimal_places=3)
    hwrateextrabed = models.DecimalField(max_digits=14, decimal_places=3)
    addonids = models.CharField(max_length=20)
    canpolicyid = models.ForeignKey(Canpolicymaster, models.DO_NOTHING, db_column='canpolicyid')
    trial_respolicyid_12 = models.ForeignKey('Reservepolicymaster', models.DO_NOTHING, db_column='trial_respolicyid_12')
    tax = models.CharField(max_length=1000)
    noshowpolicyid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ratecardchild'
        unique_together = (('ratecardid', 'roomtypeid'),)


class Ratecardmaster(models.Model):
    ratecardid = models.SmallIntegerField(primary_key=True)
    ratecardname = models.CharField(unique=True, max_length=50)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ratecardmaster'


class Ratechangedetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Ratechangeheader', models.DO_NOTHING, db_column='serialnumber')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    trial_locationcode_5 = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    commpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_commamt_9 = models.DecimalField(max_digits=14, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=14, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    saleprice = models.DecimalField(max_digits=14, decimal_places=3)
    changepercent = models.DecimalField(max_digits=7, decimal_places=2)
    trial_newsaleprice_14 = models.DecimalField(max_digits=14, decimal_places=3)
    newchild = models.CharField(max_length=11)
    changeamt = models.DecimalField(max_digits=14, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ratechangedetail'


class Ratechangeheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    trial_vchidprefix_3 = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    compareid = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='compareid')
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    trial_locationid_9 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_9')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_11 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_11')
    recorddatetime = models.DateTimeField()
    narration = models.CharField(max_length=255)
    sessionid = models.CharField(max_length=6)
    trial_qtytotal_15 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_udffield1_16 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    trial_udffield5_20 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    trial_udffield7_22 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_24 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    trial_auditdate_29 = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'ratechangeheader'


class Ratetypemaster(models.Model):
    ratetypeid = models.SmallIntegerField(primary_key=True)
    trial_ratetypename_2 = models.CharField(unique=True, max_length=15)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ratetypemaster'


class Recdcustdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Recdcustheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    remarks = models.CharField(max_length=255)
    trial_tracknumber_9 = models.CharField(unique=True, max_length=15)
    jobid = models.ForeignKey(Jobmaster, models.DO_NOTHING, db_column='jobid')
    deliverydate = models.DateTimeField()
    isscustqty = models.DecimalField(max_digits=13, decimal_places=3)
    balqty = models.DecimalField(max_digits=14, decimal_places=3)
    issuejobberqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_recdjobberqty_15 = models.DecimalField(max_digits=13, decimal_places=3)
    baljobqty = models.DecimalField(max_digits=14, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'recdcustdetail'


class Recdcustheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    trial_voucherid_6 = models.SmallIntegerField()
    trial_customerid_7 = models.CharField(max_length=5)
    trial_sessionid_8 = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    trial_locationid_10 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_10')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.SmallIntegerField()
    recorddatetime = models.DateTimeField()
    trial_qtytotal_14 = models.DecimalField(max_digits=18, decimal_places=4)
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    saleserialnumber = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'recdcustheader'


class Recdjobberdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Recdjobberheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    remarks = models.CharField(max_length=255)
    trial_tracknumber_9 = models.CharField(max_length=15)
    jobid = models.ForeignKey(Jobmaster, models.DO_NOTHING, db_column='jobid')
    issjobserialnumber = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'recdjobberdetail'


class Recdjobberheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.SmallIntegerField()
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    issjobserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_sessionid_9 = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.SmallIntegerField()
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_udffield1_16 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    trial_udffield3_18 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_25 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    trial_auditremarks_31 = models.CharField(max_length=255)
    trial_link_32 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'recdjobberheader'


class Recipientuser(models.Model):
    slno = models.IntegerField(primary_key=True)
    trial_locationid_2 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_2')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'recipientuser'


class Refmaster(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Transactionmaster', models.DO_NOTHING, db_column='serialnumber')
    accountid = models.IntegerField()
    trial_toby_4 = models.SmallIntegerField()
    reftype = models.SmallIntegerField()
    refname = models.CharField(max_length=30)
    refdate = models.DateTimeField()
    debitamount = models.DecimalField(max_digits=18, decimal_places=3)
    creditamount = models.DecimalField(max_digits=18, decimal_places=3)
    trial_isdeleted_10 = models.BooleanField()
    trial_duedate_11 = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'refmaster'


class Registration(models.Model):
    trial_companyname_1 = models.CharField(max_length=50)
    contactperson = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=35)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    address3 = models.CharField(max_length=150)
    trial_cityid_8 = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='trial_cityid_8')
    stateid = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='stateid')
    countryid = models.ForeignKey(Countrymaster, models.DO_NOTHING, db_column='countryid')
    pincode = models.CharField(max_length=20)
    trial_phone_12 = models.CharField(max_length=35)
    website = models.CharField(max_length=255)
    trial_activationkey_14 = models.CharField(max_length=55)
    activationdate = models.DateTimeField()
    trial_edition_16 = models.CharField(max_length=30)
    noofusers = models.IntegerField()
    isactive = models.BooleanField()
    daysleft = models.IntegerField()
    recorddatetime = models.DateTimeField()
    guid = models.CharField(max_length=255)
    activationkeymobi = models.CharField(max_length=55)
    activationdatemobi = models.DateTimeField()
    editionmobi = models.IntegerField()
    noofusersmobi = models.IntegerField()
    trial_isactivemobi_26 = models.BooleanField()
    daysleftmobi = models.IntegerField()
    activationkeyapi = models.CharField(max_length=55)
    editionapi = models.IntegerField()
    trial_noofusersapi_30 = models.IntegerField()
    trial_isactiveapi_31 = models.BooleanField()
    daysleftapi = models.IntegerField()
    activationdateapi = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registration'


class Reportcolumns(models.Model):
    reportid = models.SmallIntegerField(primary_key=True)
    colxml = models.TextField()

    class Meta:
        managed = False
        db_table = 'reportcolumns'


class Reportmaster(models.Model):
    formname = models.CharField(primary_key=True, max_length=50)
    formtag = models.CharField(max_length=255)
    reportxml = models.TextField()

    class Meta:
        managed = False
        db_table = 'reportmaster'
        unique_together = (('formname', 'formtag'),)


class Reservationchild(models.Model):
    serialnumber = models.ForeignKey('Roomreservationheader', models.DO_NOTHING, db_column='serialnumber')
    trial_reservationid_2 = models.CharField(max_length=15)
    trial_ratedate_3 = models.DateTimeField()
    trial_ratecardid_4 = models.ForeignKey(Ratecardmaster, models.DO_NOTHING, db_column='trial_ratecardid_4')
    roomtypeid = models.ForeignKey('Roomtypemaster', models.DO_NOTHING, db_column='roomtypeid')
    lwbaserate = models.DecimalField(max_digits=14, decimal_places=3)
    lwrateextra = models.DecimalField(max_digits=14, decimal_places=3)
    trial_lwrateextrabed_8 = models.DecimalField(max_digits=14, decimal_places=3)
    hwbaserate = models.DecimalField(max_digits=14, decimal_places=3)
    hwrateextra = models.DecimalField(max_digits=14, decimal_places=3)
    hwrateextrabed = models.DecimalField(max_digits=14, decimal_places=3)
    addonids = models.CharField(max_length=20)
    canpolicyid = models.ForeignKey(Canpolicymaster, models.DO_NOTHING, db_column='canpolicyid')
    respolicyid = models.ForeignKey('Reservepolicymaster', models.DO_NOTHING, db_column='respolicyid')
    trial_taxid_15 = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='trial_taxid_15')
    taxrate = models.DecimalField(max_digits=14, decimal_places=3)
    taxamount = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    trial_taxrate1_20 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount2_24 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount3_27 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount4_30 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_roomcharges_31 = models.DecimalField(max_digits=18, decimal_places=3)
    cancelcharges = models.DecimalField(max_digits=18, decimal_places=3)
    noshowcharges = models.DecimalField(max_digits=18, decimal_places=3)
    extrabedcharges = models.DecimalField(max_digits=18, decimal_places=3)
    discountamount = models.DecimalField(max_digits=18, decimal_places=3)
    totalamount = models.DecimalField(max_digits=18, decimal_places=3)
    extrapersoncharges = models.DecimalField(max_digits=18, decimal_places=3)
    addonid = models.SmallIntegerField()
    addoncharges = models.DecimalField(max_digits=18, decimal_places=3)
    roundoffamt = models.DecimalField(max_digits=18, decimal_places=3)
    billedto = models.SmallIntegerField()
    adults = models.SmallIntegerField()
    trial_child_43 = models.SmallIntegerField()
    addonqty = models.DecimalField(max_digits=13, decimal_places=3)
    extrabed = models.SmallIntegerField()
    noshowpolicyid = models.ForeignKey(Noshowpolicymaster, models.DO_NOTHING, db_column='noshowpolicyid')
    srlno = models.IntegerField(primary_key=True)
    trial_taxablevalue1_48 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue3_50 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue4 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'reservationchild'
        unique_together = (('trial_reservationid_2', 'trial_ratedate_3', 'addonid'),)


class Reservationdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Reservationheader', models.DO_NOTHING, db_column='serialnumber')
    trial_layoutid_3 = models.ForeignKey(Layoutmaster, models.DO_NOTHING, db_column='trial_layoutid_3')
    trial_tablename_4 = models.CharField(max_length=6)
    trial_tablestatus_5 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'reservationdetail'


class Reservationheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    bookdate = models.DateTimeField()
    trial_datefrom_3 = models.DateTimeField()
    dateto = models.DateTimeField()
    trial_customerid_5 = models.CharField(max_length=5)
    salespersonid = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='salespersonid')
    noofpax = models.SmallIntegerField()
    statusid = models.SmallIntegerField()
    remarks = models.CharField(max_length=250)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    trial_modifylocationid_12 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_modifylocationid_12')
    trial_userid_13 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_13')
    recorddatetime = models.DateTimeField()
    sessionid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'reservationheader'


class Reservepolicymaster(models.Model):
    respolicyid = models.SmallIntegerField(primary_key=True)
    respolicyname = models.CharField(unique=True, max_length=50)
    beforearrivaldays = models.SmallIntegerField()
    bookingtype = models.SmallIntegerField()
    chargedays = models.SmallIntegerField()
    chargepercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargeamt = models.DecimalField(max_digits=13, decimal_places=3)
    isfixed = models.BooleanField()
    trial_isactive_9 = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'reservepolicymaster'


class Resourcemaster(models.Model):
    resourceid = models.SmallIntegerField(primary_key=True)
    resourcename = models.CharField(unique=True, max_length=50)
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'resourcemaster'


class Restkot(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=19, decimal_places=4)
    trial_kotdatetime_2 = models.DateTimeField()
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    sessionid = models.CharField(max_length=6)
    deliverydatetime = models.DateTimeField()
    statusid = models.SmallIntegerField()
    kotidprefix = models.CharField(max_length=15)
    kotidymd = models.CharField(max_length=6)
    newkotnumber = models.IntegerField()
    orderselected = models.DateTimeField()
    orderdone = models.DateTimeField()
    trial_orderserve_14 = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'restkot'


class Restmenuchild(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    menuid = models.ForeignKey('Restmenumaster', models.DO_NOTHING, db_column='menuid')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    rate = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    stationid = models.SmallIntegerField()
    trial_kotprinter_6 = models.SmallIntegerField()
    trial_modifierid_7 = models.ForeignKey('Restmodifiermaster', models.DO_NOTHING, db_column='trial_modifierid_7')
    askprice = models.BooleanField()
    trial_maxqty_9 = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    counterid = models.ForeignKey(Countermaster, models.DO_NOTHING, db_column='counterid')
    trial_warehouseid_12 = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='trial_warehouseid_12')
    menuitemcolor = models.CharField(max_length=20)
    menuitemposition = models.SmallIntegerField()
    trial_submenuid_15 = models.SmallIntegerField()
    menugroupcolor = models.CharField(max_length=20)
    trial_menugroupposition_17 = models.SmallIntegerField()
    trial_displayname_18 = models.CharField(max_length=20)
    preparationtime = models.SmallIntegerField()
    trial_itemtype_20 = models.SmallIntegerField()
    trial_askqty_21 = models.SmallIntegerField()
    checkstock = models.SmallIntegerField()
    forcedquestionid = models.CharField(max_length=255)
    printtag = models.SmallIntegerField()
    submenu = models.CharField(max_length=50)
    isveg = models.SmallIntegerField()
    thirdpartyjson = models.TextField()
    trial_suggestitem_28 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'restmenuchild'
        unique_together = (('menuid', 'productid'),)


class Restmenulocation(models.Model):
    serialnumber = models.SmallIntegerField(primary_key=True)
    trial_menuid_2 = models.ForeignKey('Restmenumaster', models.DO_NOTHING, db_column='trial_menuid_2')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')

    class Meta:
        managed = False
        db_table = 'restmenulocation'
        unique_together = (('trial_menuid_2', 'locationid'),)


class Restmenumaster(models.Model):
    menuid = models.SmallIntegerField(primary_key=True)
    menuname = models.CharField(unique=True, max_length=50)
    menucolor = models.CharField(max_length=20)
    menuitemcolor = models.CharField(max_length=20)
    groupon = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='groupon')
    isactive = models.BooleanField()
    trial_isfixed_7 = models.BooleanField()
    menuitemnoofrows = models.SmallIntegerField()
    trial_menuitemnoofcols_9 = models.SmallIntegerField()
    trial_areaofitemscreen_10 = models.SmallIntegerField()
    menugroupnoofrows = models.SmallIntegerField()
    menugroupnoofcols = models.SmallIntegerField()
    teamid = models.CharField(max_length=50)
    fqtogether = models.SmallIntegerField()
    fqqtychange = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    trial_logsession_18 = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()
    trial_thirdpartyjson_20 = models.TextField()

    class Meta:
        managed = False
        db_table = 'restmenumaster'


class Restmodifierchild(models.Model):
    serialnumber = models.SmallIntegerField(primary_key=True)
    trial_modifierid_2 = models.ForeignKey('Restmodifiermaster', models.DO_NOTHING, db_column='trial_modifierid_2')
    trial_productid_3 = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='trial_productid_3')
    rate = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    stationid = models.SmallIntegerField()
    kotprinter = models.SmallIntegerField()
    type = models.SmallIntegerField()
    modifieritemcolor = models.CharField(max_length=20)
    modifieritemposition = models.SmallIntegerField()
    trial_submodifierid_10 = models.SmallIntegerField()
    modifiergroupcolor = models.CharField(max_length=20)
    trial_modifiergroupposition_12 = models.SmallIntegerField()
    trial_displayname_13 = models.CharField(max_length=20)
    submodifier = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'restmodifierchild'


class Restmodifiermaster(models.Model):
    modifierid = models.SmallIntegerField(primary_key=True)
    trial_modifiername_2 = models.CharField(unique=True, max_length=50)
    modifiercolor = models.CharField(max_length=20)
    trial_modifieritemcolor_4 = models.CharField(max_length=20)
    groupon = models.SmallIntegerField()
    trial_isactive_6 = models.BooleanField()
    isfixed = models.BooleanField()
    modifieritemnoofrows = models.SmallIntegerField()
    modifieritemnoofcols = models.SmallIntegerField()
    modifiergroupnoofcols = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    trial_loglocation_12 = models.SmallIntegerField()
    trial_logsession_13 = models.CharField(max_length=6)
    trial_mlnumber_14 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'restmodifiermaster'


class Roomblockdata(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    roomid = models.ForeignKey('Roommaster', models.DO_NOTHING, db_column='roomid')
    trial_blockedon_3 = models.DateTimeField()
    blockedfrom = models.DateTimeField()
    trial_blockedto_5 = models.DateTimeField()
    actualblockedfrom = models.DateTimeField()
    trial_actualblockedto_7 = models.DateTimeField()
    trial_blockedby_8 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_blockedby_8')
    blockedreason = models.CharField(max_length=500)
    trial_unblockedon_10 = models.DateTimeField()
    trial_unblockedby_11 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_unblockedby_11')
    trial_unblockedreason_12 = models.CharField(max_length=500)
    trial_locationid_13 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_13')
    sessionid = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'roomblockdata'


class Roommaster(models.Model):
    trial_roomid_1 = models.SmallIntegerField(primary_key=True)
    roomname = models.CharField(unique=True, max_length=50)
    printname = models.CharField(max_length=50)
    roomtypeid = models.ForeignKey('Roomtypemaster', models.DO_NOTHING, db_column='roomtypeid')
    trial_floorno_5 = models.SmallIntegerField()
    block = models.SmallIntegerField()
    minibar = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='minibar')
    isfixed = models.BooleanField()
    trial_isactive_9 = models.BooleanField()
    status = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'roommaster'


class Roomreservationdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Roomreservationheader', models.DO_NOTHING, db_column='serialnumber')
    roomid = models.ForeignKey(Roommaster, models.DO_NOTHING, db_column='roomid')
    customerid = models.CharField(max_length=5)
    trial_reservationid_5 = models.CharField(max_length=15)
    checkindate = models.DateTimeField()
    trial_checkoutdate_7 = models.DateTimeField()
    actualcheckin = models.DateTimeField()
    actualcheckout = models.DateTimeField()
    adults = models.SmallIntegerField()
    child = models.SmallIntegerField()
    extrabed = models.SmallIntegerField()
    ebcheckin = models.DateTimeField()
    trial_ebcheckout_14 = models.DateTimeField()
    trial_discountpercent_15 = models.DecimalField(max_digits=14, decimal_places=3)
    amount = models.DecimalField(max_digits=14, decimal_places=3)
    resstatus = models.SmallIntegerField()
    assigned = models.BooleanField()
    trial_ratecardid_19 = models.ForeignKey(Ratecardmaster, models.DO_NOTHING, db_column='trial_ratecardid_19')
    trial_addon_20 = models.CharField(max_length=20)
    averagerate = models.DecimalField(max_digits=14, decimal_places=3)
    identitytype = models.SmallIntegerField()
    idnumber = models.CharField(max_length=100)
    purpose = models.SmallIntegerField()
    trial_visanumber_25 = models.CharField(max_length=25)
    roomsharer = models.CharField(max_length=512)
    fromcity = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='fromcity')
    trial_arrivalmode_28 = models.SmallIntegerField()
    arrivalnotes = models.CharField(max_length=25)
    arrivaltime = models.CharField(max_length=5)
    pickuptime = models.CharField(max_length=5)
    pickupfrom = models.SmallIntegerField()
    tocity = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='tocity')
    departuremode = models.SmallIntegerField()
    trial_departurenotes_35 = models.CharField(max_length=25)
    departuretime = models.CharField(max_length=5)
    dropofftime = models.CharField(max_length=5)
    dropoffto = models.SmallIntegerField()
    cancellationreasonid = models.ForeignKey(Cancellationreasonmaster, models.DO_NOTHING, db_column='cancellationreasonid')
    cancellationdate = models.DateTimeField()
    ratetype = models.SmallIntegerField()
    billedto = models.SmallIntegerField()
    trial_reserveuserid_43 = models.SmallIntegerField()
    checkinuserid = models.SmallIntegerField()
    trial_checkoutuserid_45 = models.SmallIntegerField()
    trial_cvnuserid_46 = models.SmallIntegerField()
    trial_idissuedate_47 = models.DateTimeField()
    idissueplace = models.CharField(max_length=50)
    visitremarks = models.CharField(max_length=100)
    visaissuedate = models.DateTimeField()
    visaexpiredate = models.DateTimeField()
    trial_visatypeclass_52 = models.CharField(max_length=50)
    visaissueplace = models.CharField(max_length=50)
    remarks = models.CharField(max_length=500)
    folioidprefix = models.CharField(max_length=15)
    folioidymd = models.CharField(max_length=6)
    trial_folionumber_57 = models.IntegerField()
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    trial_voucherid_59 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_voucherid_59')
    regnnoprefix = models.CharField(max_length=15)
    regnnoymd = models.CharField(max_length=6)
    regnno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roomreservationdetail'
        unique_together = (('serialnumber', 'trial_reservationid_5'),)


class Roomreservationheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    narration = models.CharField(max_length=255)
    sessionid = models.CharField(max_length=6)
    trial_createlocationid_9 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_9')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    trial_modifylocationid_11 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_modifylocationid_11')
    trial_userid_12 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_12')
    trial_recorddatetime_13 = models.DateTimeField()
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_22 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    trial_auditlocation_28 = models.SmallIntegerField()
    trial_auditremarks_29 = models.CharField(max_length=255)
    trial_link_30 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    trial_batchid_32 = models.CharField(max_length=6)
    businesssource = models.SmallIntegerField()
    trial_marketplace_34 = models.SmallIntegerField()
    trial_agent_35 = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='trial_agent_35')
    trial_customerid_36 = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'roomreservationheader'


class Roomtypemaster(models.Model):
    roomtypeid = models.SmallIntegerField(primary_key=True)
    roomtypename = models.CharField(unique=True, max_length=50)
    standardoccupancy = models.SmallIntegerField()
    trial_maxoccupancy_4 = models.SmallIntegerField()
    maxextrabed = models.SmallIntegerField()
    amenities = models.CharField(max_length=50)
    roomtypeimage = models.CharField(max_length=50)
    trial_isfixed_8 = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'roomtypemaster'


class Salarystructure(models.Model):
    costcenterid = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='costcenterid')
    trial_fromdate_2 = models.DateTimeField()
    payheadid = models.ForeignKey(Payheadmaster, models.DO_NOTHING, db_column='payheadid')
    rate = models.DecimalField(max_digits=18, decimal_places=4)
    per = models.SmallIntegerField()
    isfixed = models.BooleanField()
    trial_isactive_7 = models.BooleanField()
    srlno = models.IntegerField(primary_key=True)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'salarystructure'
        unique_together = (('costcenterid', 'trial_fromdate_2', 'payheadid'),)


class Salebudget(models.Model):
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    voucherdate = models.DateTimeField()
    saleamt = models.DecimalField(max_digits=18, decimal_places=3)
    budgetamt = models.DecimalField(max_digits=18, decimal_places=3)
    saleamtwt = models.DecimalField(max_digits=18, decimal_places=3)
    budgetamtwt = models.DecimalField(max_digits=18, decimal_places=3)
    taxamt = models.DecimalField(max_digits=18, decimal_places=3)
    trial_servicetaxamt_8 = models.DecimalField(max_digits=18, decimal_places=3)
    totalbills = models.SmallIntegerField()
    totalitems = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'salebudget'
        unique_together = (('locationid', 'voucherdate'),)


class Salechallandetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Salechallanheader', models.DO_NOTHING, db_column='serialnumber')
    saletype = models.SmallIntegerField()
    trial_productid_4 = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='trial_productid_4')
    childid = models.CharField(max_length=4)
    trial_locationcode_6 = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    trial_modifierproductid_8 = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='trial_modifierproductid_8')
    trial_warehouseid_9 = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='trial_warehouseid_9')
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    trial_remarks_13 = models.CharField(max_length=255)
    salespersonid = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='salespersonid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=14, decimal_places=3)
    taxamount = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    trial_taxrate4_29 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount4_30 = models.DecimalField(max_digits=18, decimal_places=3)
    discountproduct = models.DecimalField(max_digits=14, decimal_places=3)
    discountmanual = models.DecimalField(max_digits=14, decimal_places=3)
    discountfinal = models.DecimalField(max_digits=14, decimal_places=3)
    finalsalerate = models.DecimalField(max_digits=20, decimal_places=9)
    perunitid = models.SmallIntegerField()
    isprinted = models.SmallIntegerField()
    trial_printerid_37 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='trial_printerid_37')
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    soserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    trial_inputrateperqty_46 = models.DecimalField(max_digits=13, decimal_places=3)
    productdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    customerdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_pricelistdiscount_49 = models.DecimalField(max_digits=14, decimal_places=3)
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    trial_schemeid_52 = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='trial_schemeid_52')
    schemediscpercent = models.DecimalField(max_digits=5, decimal_places=2)
    schemediscamt = models.DecimalField(max_digits=14, decimal_places=3)
    chargespercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    sal = models.DecimalField(max_digits=13, decimal_places=3)
    trial_sr_58 = models.DecimalField(max_digits=13, decimal_places=3)
    cr = models.DecimalField(max_digits=13, decimal_places=3)
    bal = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    trial_finalsaleamount_61 = models.DecimalField(max_digits=34, decimal_places=12, blank=True, null=True)
    calcmethod = models.SmallIntegerField()
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue4_66 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'salechallandetail'


class Salechallanheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    trial_noofpax_7 = models.SmallIntegerField()
    customerid = models.CharField(max_length=5)
    trial_linkcustomerid_9 = models.CharField(max_length=5)
    trial_companyname_10 = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    address3 = models.CharField(max_length=150)
    cityid = models.SmallIntegerField()
    stateid = models.SmallIntegerField()
    countryid = models.SmallIntegerField()
    pincode = models.CharField(max_length=50)
    trial_narration_18 = models.CharField(max_length=255)
    trial_roundoffamt_19 = models.DecimalField(max_digits=14, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    isprinted = models.SmallIntegerField()
    trial_companyid_22 = models.SmallIntegerField()
    trial_sessionid_23 = models.CharField(max_length=6)
    trial_createlocationid_24 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_24')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_27 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_27')
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    taxtotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_pricelistid_32 = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='trial_pricelistid_32')
    trial_duedate_33 = models.DateTimeField()
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    trial_udffield4_37 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    trial_udffield6_39 = models.CharField(max_length=50)
    trial_udffield7_40 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    trial_stationid_44 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_44')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    trial_auditlocation_48 = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    trial_link_50 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    streetnumber = models.CharField(max_length=25)
    streetid = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='streetid')
    localityid = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='localityid')
    trial_remarks_56 = models.CharField(max_length=255)
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')
    trial_businesstype_58 = models.SmallIntegerField()
    gstinnumbercustomer = models.CharField(max_length=20)
    gstinnumberecommerce = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'salechallanheader'


class Salechallanreturndetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Salechallanreturnheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    trial_saletype_3 = models.SmallIntegerField()
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    modifierproductid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='modifierproductid')
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    trial_quantity_10 = models.DecimalField(max_digits=13, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    trial_salerate_12 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_remarks_13 = models.CharField(max_length=255)
    salespersonid = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='salespersonid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=14, decimal_places=3)
    trial_taxamount_17 = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    trial_taxid1_19 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    trial_taxrate2_23 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount2_24 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxid3_25 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    trial_taxrate4_29 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount4_30 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_discountproduct_31 = models.DecimalField(max_digits=13, decimal_places=2)
    discountmanual = models.DecimalField(max_digits=14, decimal_places=3)
    discountfinal = models.DecimalField(max_digits=14, decimal_places=3)
    finalsalerate = models.DecimalField(max_digits=20, decimal_places=9)
    perunitid = models.SmallIntegerField()
    isprinted = models.SmallIntegerField()
    trial_printerid_37 = models.SmallIntegerField()
    trial_scserialnumber_38 = models.DecimalField(max_digits=18, decimal_places=4)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    trial_unitid_42 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_unitid_42')
    trial_inputrate_43 = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_productdiscount_46 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_customerdiscount_47 = models.DecimalField(max_digits=14, decimal_places=3)
    pricelistdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    schemeid = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='schemeid')
    schemediscpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_schemediscamt_53 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_chargespercent_54 = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_finalsaleamount_56 = models.DecimalField(max_digits=34, decimal_places=12, blank=True, null=True)
    calcmethod = models.SmallIntegerField()
    trial_taxablevalue1_58 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue3_60 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue4 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'salechallanreturndetail'


class Salechallanreturnheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    noofpax = models.SmallIntegerField()
    trial_customerid_8 = models.CharField(max_length=5)
    linkcustomerid = models.CharField(max_length=5)
    trial_companyname_10 = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    address3 = models.CharField(max_length=150, blank=True, null=True)
    trial_cityid_14 = models.SmallIntegerField()
    stateid = models.SmallIntegerField()
    countryid = models.SmallIntegerField()
    pincode = models.CharField(max_length=50)
    narration = models.CharField(max_length=255)
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    isprinted = models.SmallIntegerField()
    trial_companyid_22 = models.SmallIntegerField()
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    taxtotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_pricelistid_32 = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='trial_pricelistid_32')
    trial_duedate_33 = models.DateTimeField()
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    trial_udffield5_38 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    trial_udffield7_40 = models.CharField(max_length=50)
    trial_udffield8_41 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    trial_auditlocation_48 = models.SmallIntegerField()
    trial_auditremarks_49 = models.CharField(max_length=255)
    trial_link_50 = models.CharField(max_length=512)
    trial_datalastchanged_51 = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_streetnumber_53 = models.CharField(max_length=25)
    streetid = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='streetid')
    localityid = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='localityid')
    trial_remarks_56 = models.CharField(max_length=255)
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')
    businesstype = models.SmallIntegerField()
    gstinnumbercustomer = models.CharField(max_length=20)
    gstinnumberecommerce = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'salechallanreturnheader'


class Saledetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Saleheader', models.DO_NOTHING, db_column='serialnumber')
    saletype = models.SmallIntegerField()
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    modifierproductid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='modifierproductid')
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    remarks = models.CharField(max_length=255)
    salespersonid = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='salespersonid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    trial_taxrate_16 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_taxamount_17 = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    trial_taxrate1_20 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    trial_taxrate3_26 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    discountproduct = models.DecimalField(max_digits=14, decimal_places=3)
    discountmanual = models.DecimalField(max_digits=14, decimal_places=3)
    discountfinal = models.DecimalField(max_digits=14, decimal_places=3)
    trial_finalsalerate_34 = models.DecimalField(max_digits=20, decimal_places=9)
    perunitid = models.SmallIntegerField()
    trial_isprinted_36 = models.SmallIntegerField()
    menuid = models.ForeignKey(Restmenumaster, models.DO_NOTHING, db_column='menuid')
    kotnumber = models.DecimalField(max_digits=18, decimal_places=4)
    cancellationreasonid = models.SmallIntegerField()
    printerid = models.SmallIntegerField()
    trial_stationid_41 = models.SmallIntegerField()
    soserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    trial_inputrate_47 = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    productdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    customerdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    pricelistdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_spcommpercent_53 = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    schemeid = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='schemeid')
    trial_schemediscpercent_56 = models.DecimalField(max_digits=5, decimal_places=2)
    schemediscamt = models.DecimalField(max_digits=14, decimal_places=3)
    scserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_chargespercent_59 = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_finalsaleamount_61 = models.DecimalField(max_digits=34, decimal_places=12, blank=True, null=True)
    trial_seatid_62 = models.ForeignKey('Seatmaster', models.DO_NOTHING, db_column='trial_seatid_62')
    trial_voiddatetime_63 = models.DateTimeField()
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    voiduserid = models.SmallIntegerField()
    trial_ordernumber_66 = models.CharField(max_length=25)
    userstationid = models.SmallIntegerField()
    trial_calcmethod_68 = models.SmallIntegerField()
    trial_taxablevalue1_69 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue3_71 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue4 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_statusid_73 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'saledetail'


class Saleheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    trial_vchidprefix_3 = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    trial_voucherid_6 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_voucherid_6')
    layoutid = models.SmallIntegerField()
    tablename = models.CharField(max_length=15)
    noofpax = models.SmallIntegerField()
    trial_datetimein_10 = models.DateTimeField()
    trial_datetimeout_11 = models.DateTimeField()
    soserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    customerid = models.CharField(max_length=5)
    linkcustomerid = models.CharField(max_length=5)
    trial_companyname_15 = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    address3 = models.CharField(max_length=150, blank=True, null=True)
    cityid = models.SmallIntegerField()
    stateid = models.SmallIntegerField()
    countryid = models.SmallIntegerField()
    pincode = models.CharField(max_length=50)
    narration = models.CharField(max_length=255)
    billreference = models.CharField(max_length=30)
    roundoffamt = models.DecimalField(max_digits=14, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    crmpoints = models.DecimalField(max_digits=13, decimal_places=3)
    crmpointstoparent = models.DecimalField(max_digits=13, decimal_places=3)
    isprinted = models.SmallIntegerField()
    trial_saleaccountid_30 = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='trial_saleaccountid_30')
    accountserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    companyid = models.SmallIntegerField()
    sessionid = models.CharField(max_length=6)
    trial_createlocationid_34 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_34')
    trial_locationid_35 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_35')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_37 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_37')
    trial_recorddatetime_38 = models.DateTimeField()
    trial_status_39 = models.SmallIntegerField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_taxtotal_42 = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    duedate = models.DateTimeField()
    servicemodeid = models.ForeignKey('Servicemodemaster', models.DO_NOTHING, db_column='servicemodeid')
    tagoftable = models.CharField(max_length=25)
    trial_udffield1_47 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    trial_udffield3_49 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_56 = models.CharField(max_length=50)
    stationid = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='stationid')
    trial_deliverydatetime_58 = models.DateTimeField()
    trial_driverid_59 = models.SmallIntegerField()
    assigndatetime = models.DateTimeField()
    deliverdatetime = models.DateTimeField()
    deliverystatus = models.SmallIntegerField()
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    trial_auditremarks_67 = models.CharField(max_length=255)
    trial_link_68 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    reservationid = models.CharField(max_length=15)
    salemode = models.SmallIntegerField()
    discountcouponid = models.CharField(max_length=20)
    deliverytype = models.SmallIntegerField()
    addresstype = models.SmallIntegerField()
    packages = models.SmallIntegerField()
    streetnumber = models.CharField(max_length=25)
    streetid = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='streetid')
    trial_localityid_79 = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='trial_localityid_79')
    billedto = models.SmallIntegerField()
    hdserial = models.IntegerField()
    assignuser = models.SmallIntegerField()
    delivereduser = models.SmallIntegerField()
    trial_pmntuser_84 = models.SmallIntegerField()
    pmntdate = models.DateTimeField()
    prepareuser = models.SmallIntegerField()
    trial_preparedate_87 = models.DateTimeField()
    trial_tripid_88 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_remarks_89 = models.CharField(max_length=255)
    mobiwallet = models.CharField(max_length=100)
    otherswentry = models.SmallIntegerField()
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')
    businesstype = models.SmallIntegerField()
    trial_gstinnumbercustomer_94 = models.CharField(max_length=20)
    gstinnumberecommerce = models.CharField(max_length=20)
    trial_tpvchno_96 = models.CharField(max_length=50)
    tpchannel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'saleheader'


class Saleorderchild(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Saleorderheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    trial_productid_3 = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='trial_productid_3')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    trial_productchildid_6 = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    validity = models.SmallIntegerField()
    trial_activityid_9 = models.ForeignKey(Activitymaster, models.DO_NOTHING, db_column='trial_activityid_9')
    trial_reservestartdatetime_10 = models.DateTimeField()
    duration = models.SmallIntegerField()
    costcenterid = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='costcenterid')
    resourceid = models.ForeignKey(Resourcemaster, models.DO_NOTHING, db_column='resourceid')
    status = models.SmallIntegerField()
    reserveenddatetime = models.DateTimeField()
    saleserialnumber = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'saleorderchild'


class Saleorderdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Saleorderheader', models.DO_NOTHING, db_column='serialnumber')
    trial_saletype_3 = models.SmallIntegerField()
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    trial_childid_5 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    modifierproductid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='modifierproductid')
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    remarks = models.CharField(max_length=255)
    salespersonid = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='salespersonid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=14, decimal_places=3)
    taxamount = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    trial_includeinrate_18 = models.BooleanField()
    taxid1 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount1_21 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount3_27 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    taxrate4 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_discountproduct_31 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_discountmanual_32 = models.DecimalField(max_digits=14, decimal_places=3)
    discountfinal = models.DecimalField(max_digits=14, decimal_places=3)
    discountamount = models.DecimalField(max_digits=14, decimal_places=3)
    finalsalerate = models.DecimalField(max_digits=20, decimal_places=9)
    perunitid = models.SmallIntegerField()
    isprinted = models.BooleanField()
    printerid = models.SmallIntegerField()
    kotnumber = models.DecimalField(max_digits=18, decimal_places=4)
    kotdatetime = models.DateTimeField()
    trial_cancellationreasonid_41 = models.SmallIntegerField()
    isdeleted = models.BooleanField()
    sal = models.DecimalField(max_digits=13, decimal_places=3)
    sr = models.DecimalField(max_digits=13, decimal_places=3)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_alternateunitid_46 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_alternateunitid_46')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    trial_inputrate_49 = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    adj = models.DecimalField(max_digits=13, decimal_places=3)
    trial_productdiscount_53 = models.DecimalField(max_digits=14, decimal_places=3)
    customerdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_pricelistdiscount_55 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_salch_56 = models.DecimalField(max_digits=13, decimal_places=3)
    srch = models.DecimalField(max_digits=13, decimal_places=3)
    bal = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    chargespercent = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_finalsaleamount_61 = models.DecimalField(max_digits=34, decimal_places=12, blank=True, null=True)
    calcmethod = models.SmallIntegerField()
    schemeid = models.SmallIntegerField()
    schemediscpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_schemediscamt_65 = models.DecimalField(max_digits=14, decimal_places=3)
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue3_68 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_taxablevalue4_69 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'saleorderdetail'


class Saleorderheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    trial_layoutid_7 = models.SmallIntegerField()
    trial_tablename_8 = models.CharField(max_length=15)
    datetimein = models.DateTimeField()
    trial_datetimeout_10 = models.DateTimeField()
    customerid = models.CharField(max_length=5)
    linkcustomerid = models.CharField(max_length=5)
    companyname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    trial_address2_15 = models.CharField(max_length=150, blank=True, null=True)
    address3 = models.CharField(max_length=150, blank=True, null=True)
    trial_cityid_17 = models.SmallIntegerField()
    stateid = models.SmallIntegerField()
    countryid = models.SmallIntegerField()
    trial_pincode_20 = models.CharField(max_length=50)
    narration = models.CharField(max_length=255)
    billreference = models.CharField(max_length=30)
    trial_roundoffamt_23 = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    isprinted = models.SmallIntegerField()
    accountserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    companyid = models.SmallIntegerField()
    sessionid = models.CharField(max_length=6)
    isdeleted = models.BooleanField()
    trial_createlocationid_30 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_30')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_subtotal_36 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_taxtotal_37 = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    trial_deliverydate_39 = models.DateTimeField()
    trial_udffield1_40 = models.CharField(max_length=50)
    trial_udffield2_41 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    trial_stationid_50 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_50')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    trial_link_56 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_deliverytype_59 = models.SmallIntegerField()
    addresstype = models.SmallIntegerField()
    trial_packages_61 = models.SmallIntegerField()
    streetnumber = models.CharField(max_length=25)
    trial_streetid_63 = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='trial_streetid_63')
    trial_localityid_64 = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='trial_localityid_64')
    remarks = models.CharField(max_length=255)
    approvalno = models.SmallIntegerField()
    trial_placeofsupply_67 = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='trial_placeofsupply_67')
    trial_businesstype_68 = models.SmallIntegerField()
    gstinnumbercustomer = models.CharField(max_length=20)
    trial_gstinnumberecommerce_70 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'saleorderheader'


class Saleorderpayment(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey(Saleorderheader, models.DO_NOTHING, db_column='serialnumber')
    mopid = models.ForeignKey(Modeofpayment, models.DO_NOTHING, db_column='mopid')
    amount = models.DecimalField(max_digits=14, decimal_places=3)
    tenderamount = models.DecimalField(max_digits=14, decimal_places=3)
    returnamount = models.DecimalField(max_digits=14, decimal_places=3)
    documentno = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    trial_isdeleted_9 = models.BooleanField()
    refname = models.CharField(max_length=25)
    exchangerate = models.DecimalField(max_digits=23, decimal_places=10)
    trial_remarks_12 = models.CharField(max_length=500)
    trial_crmpoints_13 = models.DecimalField(max_digits=13, decimal_places=3)
    trial_response_14 = models.TextField()

    class Meta:
        managed = False
        db_table = 'saleorderpayment'
        unique_together = (('serialnumber', 'mopid'),)


class Salepayment(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey(Saleheader, models.DO_NOTHING, db_column='serialnumber')
    mopid = models.ForeignKey(Modeofpayment, models.DO_NOTHING, db_column='mopid')
    amount = models.DecimalField(max_digits=18, decimal_places=3)
    tenderamount = models.DecimalField(max_digits=18, decimal_places=3)
    returnamount = models.DecimalField(max_digits=18, decimal_places=3)
    documentno = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    isdeleted = models.BooleanField()
    trial_istip_10 = models.BooleanField()
    trial_refname_11 = models.CharField(max_length=25)
    crmpoints = models.DecimalField(max_digits=13, decimal_places=3)
    cardserial = models.IntegerField()
    trial_exchangerate_14 = models.DecimalField(max_digits=23, decimal_places=10)
    remarks = models.CharField(max_length=500)
    trial_response_16 = models.TextField()

    class Meta:
        managed = False
        db_table = 'salepayment'
        unique_together = (('serialnumber', 'mopid', 'trial_istip_10'),)


class Salereturndetail(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Salereturnheader', models.DO_NOTHING, db_column='serialnumber')
    saletype = models.SmallIntegerField()
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    trial_childid_5 = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    trial_productchildid_7 = models.CharField(max_length=11)
    modifierproductid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='modifierproductid')
    trial_warehouseid_9 = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='trial_warehouseid_9')
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    trial_mrp_11 = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    remarks = models.CharField(max_length=255)
    salespersonid = models.ForeignKey('Salespersonmaster', models.DO_NOTHING, db_column='salespersonid')
    taxid = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxid')
    taxrate = models.DecimalField(max_digits=14, decimal_places=3)
    trial_taxamount_17 = models.DecimalField(max_digits=21, decimal_places=3, blank=True, null=True)
    includeinrate = models.BooleanField()
    taxid1 = models.IntegerField()
    taxrate1 = models.DecimalField(max_digits=16, decimal_places=6)
    trial_taxamount1_21 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid2 = models.IntegerField()
    taxrate2 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid3 = models.IntegerField()
    taxrate3 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxid4 = models.IntegerField()
    trial_taxrate4_29 = models.DecimalField(max_digits=16, decimal_places=6)
    taxamount4 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_discountproduct_31 = models.DecimalField(max_digits=13, decimal_places=2)
    trial_discountmanual_32 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_discountfinal_33 = models.DecimalField(max_digits=14, decimal_places=3)
    finalsalerate = models.DecimalField(max_digits=20, decimal_places=9)
    perunitid = models.SmallIntegerField()
    trial_isprinted_36 = models.SmallIntegerField()
    menuid = models.SmallIntegerField()
    trial_kotnumber_38 = models.DecimalField(max_digits=18, decimal_places=4)
    cancellationreasonid = models.SmallIntegerField()
    printerid = models.SmallIntegerField()
    trial_soserialnumber_41 = models.DecimalField(max_digits=18, decimal_places=4)
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    trial_unitid_45 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_unitid_45')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_productdiscount_49 = models.DecimalField(max_digits=14, decimal_places=3)
    customerdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    pricelistdiscount = models.DecimalField(max_digits=14, decimal_places=3)
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_spcommamt_53 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_schemeid_54 = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='trial_schemeid_54')
    schemediscpercent = models.DecimalField(max_digits=5, decimal_places=2)
    trial_schemediscamt_56 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_chargespercent_57 = models.DecimalField(max_digits=5, decimal_places=2)
    chargesamount = models.DecimalField(max_digits=14, decimal_places=3)
    finalsaleamount = models.DecimalField(max_digits=34, decimal_places=12, blank=True, null=True)
    calcmethod = models.SmallIntegerField()
    taxablevalue1 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue2 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue3 = models.DecimalField(max_digits=18, decimal_places=3)
    taxablevalue4 = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'salereturndetail'


class Salereturnheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    trial_voucherid_6 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_voucherid_6')
    layoutid = models.SmallIntegerField()
    tablename = models.CharField(max_length=15)
    trial_noofpax_9 = models.SmallIntegerField()
    datetimein = models.DateTimeField()
    trial_datetimeout_11 = models.DateTimeField()
    trial_soserialnumber_12 = models.DecimalField(max_digits=18, decimal_places=4)
    customerid = models.CharField(max_length=5)
    trial_linkcustomerid_14 = models.CharField(max_length=5)
    companyname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    address3 = models.CharField(max_length=150, blank=True, null=True)
    cityid = models.SmallIntegerField()
    trial_stateid_20 = models.SmallIntegerField()
    countryid = models.SmallIntegerField()
    trial_pincode_22 = models.CharField(max_length=50)
    trial_narration_23 = models.CharField(max_length=255)
    billreference = models.CharField(max_length=30)
    roundoffamt = models.DecimalField(max_digits=10, decimal_places=3)
    billamount = models.DecimalField(max_digits=18, decimal_places=3)
    crmpoints = models.DecimalField(max_digits=13, decimal_places=3)
    crmpointstoparent = models.DecimalField(max_digits=13, decimal_places=3)
    trial_isprinted_29 = models.SmallIntegerField()
    saleaccountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='saleaccountid')
    accountserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    trial_companyid_32 = models.SmallIntegerField()
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    trial_locationid_35 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_35')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    trial_status_39 = models.SmallIntegerField()
    trial_qtytotal_40 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_subtotal_41 = models.DecimalField(max_digits=18, decimal_places=4)
    taxtotal = models.DecimalField(max_digits=18, decimal_places=4)
    pricelistid = models.ForeignKey(Pricelistmaster, models.DO_NOTHING, db_column='pricelistid')
    duedate = models.DateTimeField()
    servicemodeid = models.ForeignKey('Servicemodemaster', models.DO_NOTHING, db_column='servicemodeid')
    trial_udffield1_46 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    trial_udffield5_50 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    trial_udffield7_52 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_55 = models.CharField(max_length=50)
    trial_stationid_56 = models.ForeignKey('Stationmaster', models.DO_NOTHING, db_column='trial_stationid_56')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    trial_batchid_64 = models.CharField(max_length=6)
    trial_streetnumber_65 = models.CharField(max_length=25)
    trial_streetid_66 = models.ForeignKey('Streetmaster', models.DO_NOTHING, db_column='trial_streetid_66')
    localityid = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='localityid')
    trial_remarks_68 = models.CharField(max_length=255)
    placeofsupply = models.ForeignKey('Statemaster', models.DO_NOTHING, db_column='placeofsupply')
    businesstype = models.SmallIntegerField()
    trial_gstinnumbercustomer_71 = models.CharField(max_length=20)
    trial_gstinnumberecommerce_72 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'salereturnheader'


class Salereturnpayment(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey(Salereturnheader, models.DO_NOTHING, db_column='serialnumber')
    mopid = models.ForeignKey(Modeofpayment, models.DO_NOTHING, db_column='mopid')
    amount = models.DecimalField(max_digits=14, decimal_places=3)
    tenderamount = models.DecimalField(max_digits=14, decimal_places=3)
    trial_returnamount_6 = models.DecimalField(max_digits=14, decimal_places=3)
    trial_documentno_7 = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    isdeleted = models.BooleanField()
    trial_istip_10 = models.BooleanField()
    refname = models.CharField(max_length=25)
    crmpoints = models.DecimalField(max_digits=13, decimal_places=3)
    cardserial = models.IntegerField()
    exchangerate = models.DecimalField(max_digits=23, decimal_places=10)
    remarks = models.CharField(max_length=500)
    trial_response_16 = models.TextField()

    class Meta:
        managed = False
        db_table = 'salereturnpayment'
        unique_together = (('serialnumber', 'mopid', 'trial_istip_10'),)


class Salespersonmaster(models.Model):
    trial_salespersonid_1 = models.SmallIntegerField(primary_key=True)
    salespersonname = models.CharField(unique=True, max_length=35)
    salespersoninitial = models.CharField(max_length=15)
    trial_target_4 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    isactive = models.BooleanField()
    trial_isfixed_6 = models.BooleanField()
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    trial_teamid_9 = models.CharField(max_length=50)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'salespersonmaster'


class Schemechild(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    schemeid = models.ForeignKey('Schememaster', models.DO_NOTHING, db_column='schemeid')
    buyqtyfullprice = models.DecimalField(max_digits=13, decimal_places=3)
    trial_getqtydiscprice_4 = models.DecimalField(max_digits=13, decimal_places=3)
    discountedrate = models.DecimalField(max_digits=14, decimal_places=3)
    trial_discountpercent_6 = models.DecimalField(max_digits=6, decimal_places=2)
    calculationon = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='calculationon')
    trial_discountodditem_8 = models.BooleanField()
    buyamount = models.DecimalField(max_digits=18, decimal_places=3)
    discountvalue = models.DecimalField(max_digits=18, decimal_places=3)
    filename = models.CharField(max_length=255)
    trial_validitydays_12 = models.SmallIntegerField()
    productid = models.CharField(max_length=4)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    badiscountpercent = models.DecimalField(max_digits=6, decimal_places=2)
    getdisconanyqty = models.BooleanField()
    trial_applyschemeonce_17 = models.SmallIntegerField()
    points = models.DecimalField(max_digits=10, decimal_places=3)
    onvisit = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'schemechild'


class Schememaster(models.Model):
    schemeid = models.SmallIntegerField(primary_key=True)
    schemename = models.CharField(max_length=50)
    trial_schemetype_3 = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='trial_schemetype_3')
    fromdatetime = models.DateTimeField()
    trial_todatetime_5 = models.DateTimeField()
    trial_weekdays_6 = models.CharField(max_length=50)
    locationids = models.CharField(max_length=2048)
    trial_isactive_8 = models.BooleanField()
    isfixed = models.BooleanField()
    discountamount = models.DecimalField(max_digits=14, decimal_places=3)
    discountpercent = models.DecimalField(max_digits=6, decimal_places=2)
    iscoupon = models.SmallIntegerField()
    excludesg = models.CharField(max_length=1024)
    excludemop = models.CharField(max_length=150)
    trial_excludecardtype_15 = models.CharField(max_length=150)
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'schememaster'


class Seasonmaster(models.Model):
    seasonid = models.SmallIntegerField(primary_key=True)
    seasonname = models.CharField(unique=True, max_length=50)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    trial_isfixed_5 = models.BooleanField()
    trial_isactive_6 = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'seasonmaster'


class Seatmaster(models.Model):
    seatid = models.SmallIntegerField(primary_key=True)
    seatname = models.CharField(max_length=50)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'seatmaster'


class Server(models.Model):
    serverpath = models.CharField(max_length=255)
    databaseversion = models.DecimalField(max_digits=10, decimal_places=4)
    guid = models.CharField(max_length=512, blank=True, null=True)
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    version = models.CharField(max_length=15)
    mlexeversion = models.DecimalField(max_digits=10, decimal_places=4)
    currentdate = models.DateTimeField()
    mlguid = models.CharField(max_length=50)
    trial_printexeversion_9 = models.DecimalField(max_digits=10, decimal_places=4)
    dsexeversion = models.DecimalField(max_digits=10, decimal_places=4)
    servicepath = models.CharField(max_length=50)
    runningmasternumber = models.BigIntegerField()
    lastmasternumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'server'


class Serviceblockmaster(models.Model):
    trial_srlno_1 = models.SmallIntegerField(primary_key=True)
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    validity = models.SmallIntegerField()
    trial_activityid_4 = models.ForeignKey(Activitymaster, models.DO_NOTHING, db_column='trial_activityid_4')
    trial_duration_5 = models.SmallIntegerField()
    commissionon = models.DecimalField(max_digits=13, decimal_places=3)
    breakmin = models.SmallIntegerField()
    skillid = models.ForeignKey('Skillmaster', models.DO_NOTHING, db_column='skillid')
    trial_resourceids_9 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'serviceblockmaster'
        unique_together = (('productid', 'trial_activityid_4'),)


class Servicemodemaster(models.Model):
    servicemodeid = models.SmallIntegerField(primary_key=True)
    servicemodename = models.CharField(max_length=50)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'servicemodemaster'


class Sessionmaster(models.Model):
    trial_sessionid_1 = models.CharField(primary_key=True, max_length=6)
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    trial_windowsuser_3 = models.CharField(max_length=50)
    trial_computername_4 = models.CharField(max_length=50)
    dateandtime = models.DateTimeField()
    trial_enddateandtime_6 = models.DateTimeField()
    trial_locationid_7 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_7')
    trial_software_8 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sessionmaster'


class Shortcutandbutton(models.Model):
    trial_serialnumber_1 = models.IntegerField(primary_key=True)
    trial_parentmenuid_2 = models.IntegerField()
    menuid = models.IntegerField()
    trial_childmenuid_4 = models.IntegerField()
    formname = models.CharField(max_length=75)
    trial_formtag_6 = models.CharField(max_length=255)
    menucaption = models.TextField()
    caption1 = models.CharField(max_length=75)
    shortcutorbutton = models.SmallIntegerField()
    displayorder = models.DecimalField(max_digits=6, decimal_places=2)
    shortcutkey = models.CharField(max_length=10)
    trial_shiftmask_12 = models.IntegerField()
    defaultorder = models.DecimalField(max_digits=6, decimal_places=2)
    trial_modulename_14 = models.CharField(max_length=50)
    trial_applicationid_15 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'shortcutandbutton'
        unique_together = (('menuid', 'trial_childmenuid_4', 'trial_parentmenuid_2'),)


class Skillmaster(models.Model):
    skillid = models.SmallIntegerField(primary_key=True)
    skillname = models.CharField(unique=True, max_length=50)
    trial_isfixed_3 = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'skillmaster'


class Statemaster(models.Model):
    trial_stateid_1 = models.IntegerField(primary_key=True)
    statename = models.CharField(unique=True, max_length=50)
    trial_countryid_3 = models.ForeignKey(Countrymaster, models.DO_NOTHING, db_column='trial_countryid_3')
    isactive = models.BooleanField()
    trial_isfixed_5 = models.BooleanField()
    mlnumber = models.BigIntegerField()
    statecode = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'statemaster'


class Stationmaster(models.Model):
    trial_stationid_1 = models.SmallIntegerField(primary_key=True)
    stationname = models.CharField(unique=True, max_length=25)
    billprinter = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='billprinter')
    trial_kotprinter1_4 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='trial_kotprinter1_4')
    kotprinter2 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='kotprinter2')
    customerdisplay = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='customerdisplay')
    trial_cashdrawer_7 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='trial_cashdrawer_7')
    trial_pinpad_8 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='trial_pinpad_8')
    signaturecapture = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='signaturecapture')
    chequereader = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='chequereader')
    trial_isactive_11 = models.BooleanField()
    isfixed = models.BooleanField()
    trial_bcprinterid_13 = models.ForeignKey(Barcodeprintermaster, models.DO_NOTHING, db_column='trial_bcprinterid_13')
    loginscreennormal = models.CharField(max_length=500)
    trial_loginscreentouch_15 = models.CharField(max_length=500)
    trial_menuscreen_16 = models.CharField(max_length=500)
    kotprinter3 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='kotprinter3')
    kotprinter4 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='kotprinter4')
    kotprinter5 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='kotprinter5')
    kotprinter6 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='kotprinter6')
    kotprinter7 = models.ForeignKey(Oposmaster, models.DO_NOTHING, db_column='kotprinter7')
    localkot = models.BooleanField()
    deliverypopup = models.SmallIntegerField()
    allowsave = models.BooleanField()
    salevoucherid = models.SmallIntegerField()
    stationstatus = models.SmallIntegerField()
    lastfilenumber = models.IntegerField()
    kdsoptiondata = models.CharField(max_length=4000)
    mlnumber = models.BigIntegerField()
    trial_pendingorderpopup_30 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'stationmaster'


class Statusmaster(models.Model):
    statusid = models.SmallIntegerField(primary_key=True)
    trial_statusname_2 = models.CharField(unique=True, max_length=50)
    trial_orderby_3 = models.SmallIntegerField()
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'statusmaster'


class Stock(models.Model):
    trial_productid_1 = models.CharField(max_length=4)
    trial_childid_2 = models.CharField(max_length=4)
    trial_locationcode_3 = models.CharField(max_length=3)
    warehouseid = models.SmallIntegerField()
    trial_locationid_5 = models.SmallIntegerField()
    productchildid = models.CharField(max_length=11)
    pur = models.DecimalField(max_digits=18, decimal_places=3)
    pr = models.DecimalField(max_digits=18, decimal_places=3)
    sal = models.DecimalField(max_digits=18, decimal_places=3)
    trial_sr_10 = models.DecimalField(max_digits=18, decimal_places=3)
    prod = models.DecimalField(max_digits=18, decimal_places=3)
    trial_cons_12 = models.DecimalField(max_digits=18, decimal_places=3)
    trin = models.DecimalField(max_digits=18, decimal_places=3)
    trial_trout_14 = models.DecimalField(max_digits=18, decimal_places=3)
    field1 = models.CharField(max_length=50)
    field2 = models.CharField(max_length=50)
    field3 = models.CharField(max_length=50)
    trial_matrixlistid1_18 = models.IntegerField()
    matrixlistid2 = models.IntegerField()
    matrixlistid3 = models.IntegerField()
    mrp = models.DecimalField(max_digits=18, decimal_places=4)
    trial_producttypeid_22 = models.SmallIntegerField()
    purchasecost = models.DecimalField(max_digits=18, decimal_places=4)
    srate = models.DecimalField(max_digits=18, decimal_places=4)
    trial_sho_25 = models.DecimalField(max_digits=18, decimal_places=3)
    exc = models.DecimalField(max_digits=18, decimal_places=3)
    was = models.DecimalField(max_digits=18, decimal_places=3)
    op = models.DecimalField(max_digits=18, decimal_places=3)
    salch = models.DecimalField(max_digits=18, decimal_places=3)
    srch = models.DecimalField(max_digits=18, decimal_places=3)
    trial_purch_31 = models.DecimalField(max_digits=18, decimal_places=3)
    prch = models.DecimalField(max_digits=18, decimal_places=3)
    trial_quantity_33 = models.DecimalField(max_digits=33, decimal_places=3, blank=True, null=True)
    intrfrom = models.DecimalField(max_digits=18, decimal_places=3)
    intrto = models.DecimalField(max_digits=18, decimal_places=3)
    itemtype = models.SmallIntegerField()
    trial_mfgdate_37 = models.DateTimeField()
    best = models.SmallIntegerField()
    before = models.SmallIntegerField()
    expdate = models.DateTimeField()
    creationdate = models.DateTimeField()
    recorddatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock'


class Stockjournaldetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Stockjournalheader', models.DO_NOTHING, db_column='serialnumber')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    trial_locationcode_5 = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=18, decimal_places=3)
    sellingrate = models.DecimalField(max_digits=18, decimal_places=3)
    warehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='warehouseid')
    trial_pratevalue_11 = models.DecimalField(max_digits=32, decimal_places=6, blank=True, null=True)
    sratevalue = models.DecimalField(max_digits=32, decimal_places=6, blank=True, null=True)
    trial_alternateqty_13 = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    trial_inputrate_17 = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_journaltype_20 = models.SmallIntegerField()
    trial_grouprow_21 = models.IntegerField()
    workorderno = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'stockjournaldetail'


class Stockjournalheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    narration = models.CharField(max_length=255)
    trial_createlocationid_8 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_8')
    trial_locationid_9 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_9')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    sessionid = models.CharField(max_length=6)
    trial_qtytotal_14 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_frommodule_15 = models.SmallIntegerField()
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    trial_udffield5_20 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    trial_udffield8_23 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_25 = models.CharField(max_length=50)
    stationid = models.ForeignKey(Stationmaster, models.DO_NOTHING, db_column='stationid')
    trial_isaudited_27 = models.BooleanField()
    auditby = models.SmallIntegerField()
    trial_auditdate_29 = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    trial_auditremarks_31 = models.CharField(max_length=255)
    trial_link_32 = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_workorderno_35 = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'stockjournalheader'


class Stocktransferdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_serialnumber_2 = models.ForeignKey('Stocktransferheader', models.DO_NOTHING, db_column='trial_serialnumber_2')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    purchasecost = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    trial_pcostamount_11 = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    srateamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    mrpamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    fromlocationid = models.SmallIntegerField()
    fromwarehouseid = models.SmallIntegerField()
    tolocationid = models.SmallIntegerField()
    trial_towarehouseid_17 = models.SmallIntegerField()
    alternateqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_alternateunitid_19 = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='trial_alternateunitid_19')
    trial_conversionfactor_20 = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    trial_inputrateperqty_24 = models.DecimalField(max_digits=13, decimal_places=3)
    toserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    workorderno = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'stocktransferdetail'


class Stocktransferheader(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    trial_voucherid_6 = models.SmallIntegerField()
    fromlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='fromlocationid')
    fromwarehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='fromwarehouseid')
    trial_tolocationid_9 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_tolocationid_9')
    trial_towarehouseid_10 = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='trial_towarehouseid_10')
    narration = models.CharField(max_length=255)
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.SmallIntegerField()
    recorddatetime = models.DateTimeField()
    mrptotal = models.DecimalField(max_digits=18, decimal_places=4)
    pcosttotal = models.DecimalField(max_digits=18, decimal_places=4)
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    sratetotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_status_21 = models.SmallIntegerField()
    trial_udffield1_22 = models.CharField(max_length=50)
    trial_udffield2_23 = models.CharField(max_length=50)
    trial_udffield3_24 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    stationid = models.ForeignKey(Stationmaster, models.DO_NOTHING, db_column='stationid')
    toserialnumber = models.DecimalField(max_digits=18, decimal_places=4)
    isaudited = models.BooleanField()
    trial_auditby_35 = models.SmallIntegerField()
    trial_auditdate_36 = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    workorderno = models.CharField(max_length=15)
    statuschangedby = models.SmallIntegerField()
    statuschagedatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stocktransferheader'


class Stocktransferorderdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Stocktransferorderheader', models.DO_NOTHING, db_column='serialnumber')
    trial_productid_3 = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='trial_productid_3')
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    trial_productchildid_6 = models.CharField(max_length=11)
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    trial_purchasecost_8 = models.DecimalField(max_digits=14, decimal_places=3)
    salerate = models.DecimalField(max_digits=14, decimal_places=3)
    mrp = models.DecimalField(max_digits=14, decimal_places=3)
    pcostamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    srateamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    mrpamount = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True)
    trial_fromlocationid_14 = models.SmallIntegerField()
    trial_fromwarehouseid_15 = models.SmallIntegerField()
    trial_tolocationid_16 = models.SmallIntegerField()
    towarehouseid = models.SmallIntegerField()
    trial_alternateqty_18 = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='alternateunitid')
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    inputrate = models.DecimalField(max_digits=18, decimal_places=3)
    inputrateunitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='inputrateunitid')
    inputrateperqty = models.DecimalField(max_digits=13, decimal_places=3)
    trial_adj_25 = models.DecimalField(max_digits=13, decimal_places=3)
    trch = models.DecimalField(max_digits=13, decimal_places=3)
    bal = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    workorderno = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'stocktransferorderdetail'


class Stocktransferorderheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    trial_vchidprefix_3 = models.CharField(max_length=15)
    vchidymd = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    voucherid = models.SmallIntegerField()
    fromlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='fromlocationid')
    trial_fromwarehouseid_8 = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='trial_fromwarehouseid_8')
    tolocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='tolocationid')
    towarehouseid = models.ForeignKey('Warehousemaster', models.DO_NOTHING, db_column='towarehouseid')
    trial_narration_11 = models.CharField(max_length=255)
    trial_sessionid_12 = models.CharField(max_length=6)
    trial_createlocationid_13 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_13')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.SmallIntegerField()
    recorddatetime = models.DateTimeField()
    trial_mrptotal_17 = models.DecimalField(max_digits=18, decimal_places=4)
    trial_pcosttotal_18 = models.DecimalField(max_digits=18, decimal_places=4)
    qtytotal = models.DecimalField(max_digits=18, decimal_places=4)
    trial_sratetotal_20 = models.DecimalField(max_digits=18, decimal_places=4)
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    trial_udffield6_26 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    trial_udffield9_29 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    trial_stationid_31 = models.ForeignKey(Stationmaster, models.DO_NOTHING, db_column='trial_stationid_31')
    trial_isaudited_32 = models.BooleanField()
    trial_auditby_33 = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    trial_auditremarks_36 = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    trial_datalastchanged_38 = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_workorderno_40 = models.CharField(max_length=15)
    approvalno = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'stocktransferorderheader'


class Streetmaster(models.Model):
    trial_streetid_1 = models.IntegerField(primary_key=True)
    streetname = models.CharField(unique=True, max_length=50)
    cityid = models.ForeignKey(Citymaster, models.DO_NOTHING, db_column='cityid')
    stateid = models.ForeignKey(Statemaster, models.DO_NOTHING, db_column='stateid')
    pincode = models.CharField(max_length=20)
    countryid = models.ForeignKey(Countrymaster, models.DO_NOTHING, db_column='countryid')
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    localityid = models.ForeignKey(Localitymaster, models.DO_NOTHING, db_column='localityid')
    locationid = models.SmallIntegerField()
    trial_mlnumber_11 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'streetmaster'


class Subgroupmaster(models.Model):
    subgroupid = models.IntegerField(primary_key=True)
    subgroupname = models.CharField(unique=True, max_length=50)
    productgroupid = models.ForeignKey(Productgroupmaster, models.DO_NOTHING, db_column='productgroupid')
    matrixid = models.ForeignKey(Matrixmaster, models.DO_NOTHING, db_column='matrixid')
    taxidsale = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidsale')
    taxidpurchase = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidpurchase')
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    isactive = models.BooleanField()
    trial_isfixed_9 = models.BooleanField()
    trial_spcommpercent_10 = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    mlnumber = models.BigIntegerField()
    trial_taxslabsale_13 = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'subgroupmaster'


class Subscriptionmaster(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    customerid = models.CharField(max_length=5)
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    trial_startdate_4 = models.DateTimeField()
    enddate = models.DateTimeField()
    rate = models.DecimalField(max_digits=14, decimal_places=3)
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')

    class Meta:
        managed = False
        db_table = 'subscriptionmaster'
        unique_together = (('serialnumber', 'customerid', 'productid'),)


class Sysapplicationmaster(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    applicationid = models.IntegerField()
    applicationname = models.CharField(max_length=50)
    groupon = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Designationcategory, models.DO_NOTHING, db_column='categoryid')
    orderby = models.DecimalField(max_digits=13, decimal_places=4)
    httpmethod = models.CharField(max_length=10)
    apiapplicationname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sysapplicationmaster'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    trial_principal_id_2 = models.IntegerField()
    trial_diagram_id_3 = models.IntegerField(primary_key=True)
    trial_version_4 = models.IntegerField(blank=True, null=True)
    trial_definition_5 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('trial_principal_id_2', 'name'),)


class Tablemaster(models.Model):
    serialnumber = models.IntegerField()
    tableid = models.IntegerField(primary_key=True)
    tablename = models.TextField()
    trial_caption_4 = models.CharField(max_length=50)
    depandanttableid = models.IntegerField()
    entryedit = models.SmallIntegerField()
    idgenerate = models.SmallIntegerField()
    idforbutton = models.SmallIntegerField()
    trial_displayid_9 = models.SmallIntegerField()
    defaultviewid = models.IntegerField()
    optionid = models.SmallIntegerField()
    optiontype = models.SmallIntegerField()
    trial_optiontypeid_13 = models.SmallIntegerField()
    noofrow = models.SmallIntegerField()
    helptopicid = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tablemaster'


class Taskdata(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    trial_voucherdate_2 = models.DateTimeField()
    trial_roomid_3 = models.ForeignKey(Roommaster, models.DO_NOTHING, db_column='trial_roomid_3')
    taskid = models.IntegerField()
    trial_remarks_5 = models.CharField(max_length=500)
    duedatetime = models.DateTimeField()
    trial_assignedto_7 = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='trial_assignedto_7')
    taskstatus = models.SmallIntegerField()
    trial_departmentid_9 = models.IntegerField()
    roomstatus = models.SmallIntegerField()
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    trial_doneon_12 = models.DateTimeField()
    trial_assignedon_13 = models.DateTimeField()
    assignedby = models.IntegerField()
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    trial_modifylocationid_16 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_modifylocationid_16')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    sessionid = models.CharField(max_length=6)
    createdon = models.DateTimeField()
    modifiedon = models.DateTimeField()
    modifiedby = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'taskdata'


class Taxchild(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    trial_taxid_2 = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='trial_taxid_2')
    accountid = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='accountid')
    trial_taxvalue_4 = models.DecimalField(max_digits=16, decimal_places=6)
    userinputvalue = models.DecimalField(max_digits=13, decimal_places=3)
    trial_taxtype_6 = models.SmallIntegerField()
    calcmethod = models.SmallIntegerField()
    taxonamtpercent = models.DecimalField(max_digits=7, decimal_places=3)
    displayorder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'taxchild'


class Taxibooking(models.Model):
    serialnumber = models.OneToOneField(Saleheader, models.DO_NOTHING, db_column='serialnumber', primary_key=True)
    trial_taxinumber_2 = models.CharField(max_length=20)
    trial_paid_3 = models.DecimalField(max_digits=18, decimal_places=3)
    comptype = models.SmallIntegerField()
    complaint = models.CharField(max_length=500)
    trial_compdate_6 = models.DateTimeField()
    trial_resolution_7 = models.CharField(max_length=500)
    resodate = models.DateTimeField()
    status = models.SmallIntegerField()
    trial_paiddate_10 = models.DateTimeField()
    datalastchanged = models.BinaryField()
    assignuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='assignuserid')
    trial_paymentuserid_13 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_paymentuserid_13')
    complaintuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='complaintuserid')
    resolutionuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='resolutionuserid')
    trial_laneno_16 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'taxibooking'


class Taxmaster(models.Model):
    taxid = models.SmallIntegerField(primary_key=True)
    taxname = models.CharField(unique=True, max_length=50)
    includeinrate = models.BooleanField()
    taxvalue = models.DecimalField(max_digits=13, decimal_places=3)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    trial_calcmethod_7 = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    trial_loglocation_9 = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    trial_mlnumber_11 = models.BigIntegerField()
    trial_interstatetaxid_12 = models.SmallIntegerField()
    saleaccountid = models.IntegerField()
    salereturnaccountid = models.IntegerField()
    purchaseaccountid = models.IntegerField()
    purchasereturnaccountid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxmaster'


class Taxtypemaster(models.Model):
    taxtypeid = models.SmallIntegerField(primary_key=True)
    trial_taxtypename_2 = models.CharField(unique=True, max_length=30)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'taxtypemaster'


class Teammaster(models.Model):
    trial_teamid_1 = models.IntegerField(primary_key=True)
    teamname = models.CharField(unique=True, max_length=50)
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'teammaster'


class Templatemaster(models.Model):
    srlno = models.IntegerField(primary_key=True)
    trial_templatename_2 = models.CharField(unique=True, max_length=50)
    trial_data_3 = models.TextField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    userid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='userid')
    trial_templatedate_7 = models.DateTimeField()
    transactiontype = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'templatemaster'


class Tempstocktable(models.Model):
    productid = models.CharField(max_length=4)
    childid = models.CharField(max_length=4)
    locationcode = models.CharField(max_length=3)
    productchildid = models.CharField(max_length=11)
    trial_warehouseid_5 = models.SmallIntegerField()
    trial_locationid_6 = models.SmallIntegerField()
    con = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    pro = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    sho = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    exc = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trial_was_11 = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    pur = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    pr = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    purch = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trial_prch_15 = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trial_sal_16 = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    sr = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    salch = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    srch = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trin = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trout = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    intransit = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    ope = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    currclo = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    opein = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    qty = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trial_qtyin_27 = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
    trial_salval_28 = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
    trial_purval_29 = models.DecimalField(max_digits=38, decimal_places=6, blank=True, null=True)
    purdatemin = models.DateTimeField(blank=True, null=True)
    purdatemax = models.DateTimeField(blank=True, null=True)
    saldatemin = models.DateTimeField(blank=True, null=True)
    saldatemax = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempstocktable'


class Temptablemail0000Zn(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zn'


class Temptablemail0000Zo(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zo'


class Temptablemail0000Zp(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zp'


class Temptablemail0000Zq(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zq'


class Temptablemail0000Zr(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zr'


class Temptablemail0000Zs(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zs'


class Temptablemail0000Zt(models.Model):
    accountid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'temptablemail0000zt'


class Transactionchild(models.Model):
    trial_srlno_1 = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Transactionmaster', models.DO_NOTHING, db_column='serialnumber')
    toby = models.SmallIntegerField()
    trial_accountid_4 = models.ForeignKey(Accountmaster, models.DO_NOTHING, db_column='trial_accountid_4')
    costcenterid = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='costcenterid')
    contraid = models.IntegerField()
    trial_debitamount_7 = models.DecimalField(max_digits=18, decimal_places=3)
    trial_creditamount_8 = models.DecimalField(max_digits=18, decimal_places=3)
    reconciliationdate = models.DateTimeField()
    assessablevalue = models.DecimalField(max_digits=18, decimal_places=3)
    narration = models.TextField()

    class Meta:
        managed = False
        db_table = 'transactionchild'


class Transactionmaster(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    trial_vchnumber_5 = models.IntegerField()
    voucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='voucherid')
    narration = models.TextField()
    trial_userid_8 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_8')
    sessionid = models.CharField(max_length=6)
    trial_isdeleted_10 = models.BooleanField()
    trial_createlocationid_11 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_createlocationid_11')
    trial_locationid_12 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_12')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_isopening_14 = models.BooleanField()
    recorddatetime = models.DateTimeField()
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    udffield4 = models.CharField(max_length=50)
    udffield5 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    udffield7 = models.CharField(max_length=50)
    trial_udffield8_23 = models.CharField(max_length=50)
    trial_udffield9_24 = models.CharField(max_length=50)
    udffield10 = models.CharField(max_length=50)
    trial_stationid_26 = models.ForeignKey(Stationmaster, models.DO_NOTHING, db_column='trial_stationid_26')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    trial_auditlocation_30 = models.SmallIntegerField()
    auditremarks = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_reservationid_35 = models.CharField(max_length=15)
    trial_billedto_36 = models.SmallIntegerField()
    trial_foliono_37 = models.CharField(max_length=50)
    regnno = models.CharField(max_length=50)
    trial_she_39 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'transactionmaster'


class Tripmaster(models.Model):
    trial_serialnumber_1 = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    trial_userid_5 = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='trial_userid_5')
    vehicleid = models.ForeignKey('Vehiclemaster', models.DO_NOTHING, db_column='vehicleid')
    trial_startingmeter_7 = models.IntegerField()
    trial_datetimeout_8 = models.DateTimeField()
    trial_endingmeter_9 = models.IntegerField()
    datetimein = models.DateTimeField()
    outuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='outuserid')
    inuserid = models.ForeignKey('Usermaster', models.DO_NOTHING, db_column='inuserid')
    trial_triptype_13 = models.SmallIntegerField()
    delayreason = models.SmallIntegerField()
    trial_insessionid_15 = models.CharField(max_length=6)
    recorddatetime = models.DateTimeField()
    instationid = models.SmallIntegerField()
    datalastchanged = models.BinaryField()
    trial_outsessionid_19 = models.CharField(max_length=6)
    trial_outstationid_20 = models.SmallIntegerField()
    trial_worktype_21 = models.IntegerField()
    cancel = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tripmaster'


class Udfmaster(models.Model):
    trial_udfmoduleid_1 = models.SmallIntegerField(primary_key=True)
    trial_udfmodulename_2 = models.CharField(max_length=30)
    fieldcaption1 = models.CharField(max_length=25)
    fieldinputmethod1 = models.SmallIntegerField()
    listid1 = models.SmallIntegerField()
    trial_fieldcaption2_6 = models.CharField(max_length=25)
    fieldinputmethod2 = models.SmallIntegerField()
    listid2 = models.SmallIntegerField()
    trial_fieldcaption3_9 = models.CharField(max_length=25)
    fieldinputmethod3 = models.SmallIntegerField()
    trial_listid3_11 = models.SmallIntegerField()
    trial_fieldcaption4_12 = models.CharField(max_length=25)
    fieldinputmethod4 = models.SmallIntegerField()
    listid4 = models.SmallIntegerField()
    fieldcaption5 = models.CharField(max_length=25)
    fieldinputmethod5 = models.SmallIntegerField()
    listid5 = models.SmallIntegerField()
    fieldcaption6 = models.CharField(max_length=25)
    fieldinputmethod6 = models.SmallIntegerField()
    listid6 = models.SmallIntegerField()
    fieldcaption7 = models.CharField(max_length=25)
    trial_fieldinputmethod7_22 = models.SmallIntegerField()
    listid7 = models.SmallIntegerField()
    trial_fieldcaption8_24 = models.CharField(max_length=25)
    trial_fieldinputmethod8_25 = models.SmallIntegerField()
    trial_listid8_26 = models.SmallIntegerField()
    trial_fieldcaption9_27 = models.CharField(max_length=25)
    trial_fieldinputmethod9_28 = models.SmallIntegerField()
    trial_listid9_29 = models.SmallIntegerField()
    fieldcaption10 = models.CharField(max_length=25)
    fieldinputmethod10 = models.SmallIntegerField()
    trial_listid10_32 = models.SmallIntegerField()
    linkfieldname = models.CharField(max_length=35)
    trial_mlnumber_34 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'udfmaster'


class Unitmaster(models.Model):
    unitid = models.SmallIntegerField(primary_key=True)
    unitname = models.CharField(unique=True, max_length=20)
    formalname = models.CharField(max_length=25)
    digitafterdecimal = models.SmallIntegerField()
    conversionunit = models.SmallIntegerField()
    conversionqty = models.DecimalField(max_digits=13, decimal_places=3)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'unitmaster'


class Userlog(models.Model):
    serialnumber = models.IntegerField()
    trial_userid_2 = models.OneToOneField('Usermaster', models.DO_NOTHING, db_column='trial_userid_2')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    trial_sessionid_4 = models.ForeignKey(Sessionmaster, models.DO_NOTHING, db_column='trial_sessionid_4')
    computername = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'userlog'


class Usermaster(models.Model):
    trial_userid_1 = models.SmallIntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    trial_printname_3 = models.CharField(max_length=50, blank=True, null=True)
    trial_password_4 = models.CharField(max_length=90, blank=True, null=True)
    designationid = models.ForeignKey(Designationmaster, models.DO_NOTHING, db_column='designationid')
    defaultscreen = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='defaultscreen')
    contravoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='contravoucherid')
    trial_journalvoucherid_8 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_journalvoucherid_8')
    paymentvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='paymentvoucherid')
    receiptvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='receiptvoucherid')
    accopeningvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='accopeningvoucherid')
    physicalstockvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='physicalstockvoucherid')
    stockjournalvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='stockjournalvoucherid')
    purchasevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='purchasevoucherid')
    purchasereturnvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='purchasereturnvoucherid')
    salevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='salevoucherid')
    salereturnvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='salereturnvoucherid')
    stocktransfervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='stocktransfervoucherid')
    openingstockvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='openingstockvoucherid')
    saleordervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='saleordervoucherid')
    trial_purchaseordervoucherid_21 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_purchaseordervoucherid_21')
    trial_isactive_22 = models.BooleanField()
    isfixed = models.BooleanField()
    receivefromcustomerid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='receivefromcustomerid')
    trial_issuetojobberid_25 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_issuetojobberid_25')
    trial_receivefromjobberid_26 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_receivefromjobberid_26')
    trial_issuetocustomerid_27 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_issuetocustomerid_27')
    trial_purchasechallanid_28 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_purchasechallanid_28')
    rejectionoutid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='rejectionoutid')
    salechallanid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='salechallanid')
    rejectioninid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='rejectioninid')
    ratechangeid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='ratechangeid')
    prepaidid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='prepaidid')
    trial_email_34 = models.CharField(max_length=255)
    trial_mobile_35 = models.CharField(max_length=50)
    trial_canlogin_36 = models.BooleanField()
    locationid = models.SmallIntegerField()
    trial_stocktransferordervoucherid_38 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_stocktransferordervoucherid_38')
    usertype = models.SmallIntegerField()
    trial_debitnotevoucherid_40 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_debitnotevoucherid_40')
    trial_creditnotevoucherid_41 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_creditnotevoucherid_41')
    attendancevoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='attendancevoucherid')
    payrollvoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='payrollvoucherid')
    fingerscan = models.TextField()
    trial_roomreservationvoucherid_45 = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='trial_roomreservationvoucherid_45')
    workordervoucherid = models.ForeignKey('Vouchermaster', models.DO_NOTHING, db_column='workordervoucherid')
    inout = models.SmallIntegerField()
    teamid = models.ForeignKey(Teammaster, models.DO_NOTHING, db_column='teamid')
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    trial_logsession_51 = models.CharField(max_length=6)
    defaultscreenmobi = models.SmallIntegerField()
    trial_mlnumber_53 = models.BigIntegerField()
    allowlogininmobi = models.BooleanField()
    teamidreport = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usermaster'


class Useroption(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    parentoptionid = models.IntegerField()
    childoptionid = models.IntegerField()
    optionid = models.IntegerField()
    optionname = models.CharField(max_length=100)
    userid = models.SmallIntegerField()
    displayorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'useroption'
        unique_together = (('parentoptionid', 'childoptionid'),)


class Vatclassmaster(models.Model):
    vatclassid = models.SmallIntegerField(primary_key=True)
    vatclassname = models.CharField(max_length=100)
    isfixed = models.BooleanField()
    trial_isactive_4 = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vatclassmaster'


class Vehiclemaster(models.Model):
    trial_vehicleid_1 = models.IntegerField(primary_key=True)
    vehiclename = models.CharField(max_length=50)
    isactive = models.BooleanField()
    trial_isfixed_4 = models.BooleanField()
    registrationno = models.CharField(max_length=50)
    trial_checkmeter_6 = models.SmallIntegerField()
    trial_mlnumber_7 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vehiclemaster'


class Viewchild(models.Model):
    serialnumber = models.IntegerField(primary_key=True)
    viewid = models.ForeignKey('Viewmaster', models.DO_NOTHING, db_column='viewid')
    fieldid = models.ForeignKey(Fieldmaster, models.DO_NOTHING, db_column='fieldid')
    toporbottom = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'viewchild'
        unique_together = (('viewid', 'fieldid'),)


class Viewmaster(models.Model):
    trial_viewid_1 = models.IntegerField(primary_key=True)
    trial_viewname_2 = models.CharField(unique=True, max_length=35)
    tableid = models.ForeignKey(Tablemaster, models.DO_NOTHING, db_column='tableid')
    trial_orderby_4 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'viewmaster'


class Votemaster(models.Model):
    trial_voteid_1 = models.SmallIntegerField(primary_key=True)
    votedate = models.DateTimeField()
    trial_electionid_3 = models.ForeignKey(Electionmaster, models.DO_NOTHING, db_column='trial_electionid_3')
    postid = models.ForeignKey(Postmaster, models.DO_NOTHING, db_column='postid')
    contestant = models.CharField(max_length=5)
    trial_voterid_6 = models.CharField(max_length=5)
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'votemaster'


class Votestatus(models.Model):
    trial_srlno_1 = models.SmallIntegerField(primary_key=True)
    electionid = models.ForeignKey(Electionmaster, models.DO_NOTHING, db_column='electionid')
    trial_voterid_3 = models.CharField(max_length=5)
    status = models.SmallIntegerField()
    trial_locationid_5 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_5')
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'votestatus'


class Vouchermaster(models.Model):
    voucherid = models.SmallIntegerField(primary_key=True)
    trial_vouchername_2 = models.CharField(unique=True, max_length=50)
    trial_vouchertypeid_3 = models.ForeignKey('Vouchertypemaster', models.DO_NOTHING, db_column='trial_vouchertypeid_3')
    startingnumber = models.IntegerField()
    trial_prefix_5 = models.CharField(max_length=10)
    numbersystemid = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='numbersystemid')
    voucheroptionid = models.SmallIntegerField()
    trial_printoptionid_8 = models.SmallIntegerField()
    isfixed = models.BooleanField()
    trial_isactive_10 = models.BooleanField()
    voucheroption = models.TextField()
    trial_winprintoption_12 = models.TextField()
    trial_posprintoption_13 = models.TextField()
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    trial_logsession_16 = models.CharField(max_length=6)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vouchermaster'


class Vouchertypemaster(models.Model):
    trial_vouchertypeid_1 = models.SmallIntegerField(primary_key=True)
    trial_vouchertypename_2 = models.CharField(unique=True, max_length=50)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vouchertypemaster'


class Walkins(models.Model):
    slno = models.IntegerField(primary_key=True)
    trial_date_2 = models.DateTimeField()
    trial_locationid_3 = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='trial_locationid_3')
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'walkins'
        unique_together = (('trial_date_2', 'trial_locationid_3'),)


class Warehousemaster(models.Model):
    trial_warehouseid_1 = models.SmallIntegerField(primary_key=True)
    warehousename = models.CharField(unique=True, max_length=100)
    printname = models.CharField(max_length=100)
    trial_isactive_4 = models.BooleanField()
    isfixed = models.BooleanField()
    locationids = models.CharField(max_length=2048)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'warehousemaster'


class Workorderdetail(models.Model):
    srlno = models.IntegerField(primary_key=True)
    serialnumber = models.ForeignKey('Workorderheader', models.DO_NOTHING, db_column='serialnumber')
    productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid')
    quantity = models.DecimalField(max_digits=13, decimal_places=3)
    remarks = models.CharField(max_length=255)
    workorderno = models.CharField(max_length=15)
    status = models.SmallIntegerField()
    warehouseid = models.ForeignKey(Warehousemaster, models.DO_NOTHING, db_column='warehouseid')
    employeeid = models.ForeignKey(Costcentermaster, models.DO_NOTHING, db_column='employeeid')
    proddate = models.DateTimeField()
    trial_closedate_11 = models.DateTimeField()
    closeuser = models.SmallIntegerField()
    stockjournalserialnumber = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'workorderdetail'


class Workorderheader(models.Model):
    serialnumber = models.DecimalField(primary_key=True, max_digits=18, decimal_places=4)
    voucherdate = models.DateTimeField()
    vchidprefix = models.CharField(max_length=15)
    trial_vchidymd_4 = models.CharField(max_length=6)
    vchnumber = models.IntegerField()
    trial_voucherid_6 = models.ForeignKey(Vouchermaster, models.DO_NOTHING, db_column='trial_voucherid_6')
    sessionid = models.CharField(max_length=6)
    createlocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='createlocationid')
    locationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='locationid')
    modifylocationid = models.ForeignKey(Locationmaster, models.DO_NOTHING, db_column='modifylocationid')
    userid = models.ForeignKey(Usermaster, models.DO_NOTHING, db_column='userid')
    recorddatetime = models.DateTimeField()
    udffield1 = models.CharField(max_length=50)
    udffield2 = models.CharField(max_length=50)
    udffield3 = models.CharField(max_length=50)
    trial_udffield4_16 = models.CharField(max_length=50)
    trial_udffield5_17 = models.CharField(max_length=50)
    udffield6 = models.CharField(max_length=50)
    trial_udffield7_19 = models.CharField(max_length=50)
    udffield8 = models.CharField(max_length=50)
    udffield9 = models.CharField(max_length=50)
    trial_udffield10_22 = models.CharField(max_length=50)
    trial_stationid_23 = models.ForeignKey(Stationmaster, models.DO_NOTHING, db_column='trial_stationid_23')
    isaudited = models.BooleanField()
    auditby = models.SmallIntegerField()
    auditdate = models.DateTimeField()
    auditlocation = models.SmallIntegerField()
    trial_auditremarks_28 = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    datalastchanged = models.BinaryField()
    batchid = models.CharField(max_length=6)
    trial_narration_32 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'workorderheader'


class Workplanchild(models.Model):
    srlno = models.SmallIntegerField(primary_key=True)
    trial_workplanid_2 = models.ForeignKey('Workplanmaster', models.DO_NOTHING, db_column='trial_workplanid_2')
    weekday = models.SmallIntegerField()
    fromtime = models.CharField(max_length=8)
    totime = models.CharField(max_length=8)
    breaktime = models.CharField(max_length=8)
    trial_fromtime1_7 = models.CharField(max_length=8)
    trial_totime1_8 = models.CharField(max_length=8)
    fromtime2 = models.CharField(max_length=8)
    totime2 = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'workplanchild'
        unique_together = (('trial_workplanid_2', 'weekday'),)


class Workplanmaster(models.Model):
    workplanid = models.SmallIntegerField(primary_key=True)
    workplanname = models.CharField(unique=True, max_length=50)
    isactive = models.BooleanField()
    trial_isfixed_4 = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'workplanmaster'


class Yesnomaster(models.Model):
    trial_yesnoid_1 = models.SmallIntegerField()
    yesnoname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'yesnomaster'
