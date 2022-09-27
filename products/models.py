from django.db import models

class Principalcompanymaster(models.Model):
    principalcompanyid = models.AutoField(primary_key=True)
    principalcompanyname = models.TextField(unique=True)
    trial_isactive_3 = models.BigIntegerField()
    trial_isfixed_4 = models.BigIntegerField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'principalcompanymaster'
        
class Brandmaster(models.Model):
    trial_brandid_1 = models.AutoField(primary_key=True)
    brandname = models.TextField(unique=True)
    principalcompanyid = models.ForeignKey('Principalcompanymaster', models.DO_NOTHING, db_column='principalcompanyid')
    areaallotted = models.TextField()  # This field type is a guess.
    trial_isfixed_5 = models.BigIntegerField()
    trial_isactive_6 = models.BigIntegerField()
    spcommpercent = models.TextField()  # This field type is a guess.
    spcommamt = models.TextField()  # This field type is a guess.
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'brandmaster'

class Departmentmaster(models.Model):
    departmentid = models.AutoField(primary_key=True)
    departmentname = models.TextField(unique=True)
    areaallotted = models.TextField()  # This field type is a guess.
    isactive = models.BigIntegerField()
    trial_isfixed_5 = models.BigIntegerField()
    trial_mlnumber_6 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'departmentmaster'


class Productgroupmaster(models.Model):
    trial_productgroupid_1 = models.AutoField(primary_key=True)
    productgroupname = models.TextField(unique=True)
    departmentid = models.ForeignKey(Departmentmaster, models.DO_NOTHING, db_column='departmentid')
    areaallotted = models.TextField()  # This field type is a guess.
    trial_isactive_5 = models.BigIntegerField()
    isfixed = models.BigIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'productgroupmaster'


class Formatmaster(models.Model):
    formatid = models.AutoField(primary_key=True)
    formattype = models.TextField()
    vbprefix = models.TextField()
    vbsuffix = models.TextField()
    trial_sqlprefix_5 = models.TextField()
    sqlsuffix = models.TextField()

    class Meta:
        managed = False
        db_table = 'formatmaster'

class Listmaster(models.Model):
    listid = models.AutoField(primary_key=True)
    trial_listname_2 = models.TextField(unique=True)
    isfixed = models.BigIntegerField()
    trial_isactive_4 = models.BigIntegerField()
    trial_mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'listmaster'

class Datatypemaster(models.Model):
    datatypeid = models.AutoField(primary_key=True)
    trial_datatypename_2 = models.TextField(unique=True)
    datatypeformat = models.TextField()
    display = models.TextField()
    trial_prefixsuffix_5 = models.TextField()

    class Meta:
        managed = False
        db_table = 'datatypemaster'

class Matrixmaster(models.Model):
    matrixid = models.AutoField(primary_key=True)
    trial_matrixname_2 = models.TextField(unique=True)
    field1name = models.TextField()
    trial_field1listid_4 = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='trial_field1listid_4', related_name='trial_field1listid_4')
    field2name = models.TextField()
    trial_field2listid_6 = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='trial_field2listid_6',  related_name='trial_field2listid_6')
    field3name = models.TextField()
    field3listid = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='field3listid', related_name='field3listid')
    trial_field4name_9 = models.TextField()
    field4datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field4datatypeid', related_name='field4datatypeid')
    field5name = models.TextField()
    field5datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field5datatypeid' , related_name='field5datatypeid')
    field6name = models.TextField()
    field6datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field6datatypeid', related_name='field6datatypeid')
    isactive = models.BigIntegerField()
    isfixed = models.BigIntegerField()
    linkfieldname = models.TextField()
    activateexpiry = models.BigIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'matrixmaster'

class Subgroupmaster(models.Model):
    subgroupid = models.AutoField(primary_key=True)
    subgroupname = models.TextField(unique=True)
    productgroupid = models.ForeignKey(Productgroupmaster, models.DO_NOTHING, db_column='productgroupid')
    matrixid = models.ForeignKey(Matrixmaster, models.DO_NOTHING, db_column='matrixid')
    taxidsale = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidsale', related_name='subgroupmastertaxidsale')
    taxidpurchase = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidpurchase')
    areaallotted = models.TextField()  # This field type is a guess.
    isactive = models.BigIntegerField()
    trial_isfixed_9 = models.BigIntegerField()
    trial_spcommpercent_10 = models.TextField()  # This field type is a guess.
    spcommamt = models.TextField()  # This field type is a guess.
    mlnumber = models.BigIntegerField()
    trial_taxslabsale_13 = models.TextField()

    class Meta:
        managed = False
        db_table = 'subgroupmaster'


class Hsnsacmaster(models.Model):
    hsnsacid = models.AutoField(primary_key=True)
    hsnsaccode = models.TextField(unique=True)
    hsnsacname = models.TextField()
    isactive = models.BigIntegerField()
    isfixed = models.BigIntegerField()
    mlnumber = models.BigIntegerField()
    uqc = models.TextField()

    class Meta:
        managed = False
        db_table = 'hsnsacmaster'


class Unitmaster(models.Model):
    unitid = models.AutoField(primary_key=True)
    unitname = models.TextField(unique=True)
    formalname = models.TextField()
    digitafterdecimal = models.BigIntegerField()
    conversionunit = models.BigIntegerField()
    conversionqty = models.TextField()  # This field type is a guess.
    isactive = models.BigIntegerField()
    isfixed = models.BigIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'unitmaster'


class Taxmaster(models.Model):
    taxid = models.AutoField(primary_key=True)
    taxname = models.TextField(unique=True)
    includeinrate = models.BigIntegerField()
    taxvalue = models.TextField()  # This field type is a guess.
    isactive = models.BigIntegerField()
    isfixed = models.BigIntegerField()
    trial_calcmethod_7 = models.BigIntegerField()
    loguser = models.BigIntegerField()
    trial_loglocation_9 = models.BigIntegerField()
    logsession = models.TextField()
    trial_mlnumber_11 = models.BigIntegerField()
    trial_interstatetaxid_12 = models.BigIntegerField()
    saleaccountid = models.BigIntegerField()
    salereturnaccountid = models.BigIntegerField()
    purchaseaccountid = models.BigIntegerField()
    purchasereturnaccountid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'taxmaster'


class Productmaster(models.Model):
    id = models.TextField(primary_key=True)
    productname = models.TextField(unique=True, blank=True, null=True)
    printname = models.TextField(blank=True, null=True)
    upcean = models.TextField(unique=True)
    trial_userdefinedcode_5 = models.TextField()
    trial_maxretailprice_6 = models.TextField()  # This field type is a guess.
    trial_brandid_7 = models.ForeignKey(Brandmaster, models.DO_NOTHING, db_column='trial_brandid_7')
    subgroupid = models.ForeignKey(Subgroupmaster, models.DO_NOTHING, db_column='subgroupid')
    productgroupid = models.ForeignKey(Productgroupmaster, models.DO_NOTHING, db_column='productgroupid')
    departmentid = models.ForeignKey(Departmentmaster, models.DO_NOTHING, db_column='departmentid')
    unitid = models.ForeignKey(Unitmaster, models.DO_NOTHING, db_column='unitid')
    trial_binlocation_12 = models.TextField()
    trial_matrixid_13 = models.ForeignKey(Matrixmaster, models.DO_NOTHING, db_column='trial_matrixid_13')
    evalcount = models.BigIntegerField()
    taxidpurchase = models.ForeignKey(Taxmaster, models.DO_NOTHING, db_column='taxidpurchase', related_name='taxidpurchase')
    taxidsale = models.ForeignKey(Taxmaster, models.DO_NOTHING, db_column='taxidsale', related_name='taxidsale')
    trial_printbarcode_17 = models.BigIntegerField()
    askrate = models.BigIntegerField()
    trial_usefifo_19 = models.BigIntegerField()
    productmessage = models.TextField()
    quantityonhand = models.TextField()  # This field type is a guess.
    trial_reorderinformation_22 = models.BigIntegerField()
    reorderlevel = models.TextField()  # This field type is a guess.
    trial_safetylevel_24 = models.TextField()  # This field type is a guess.
    reorderquantity = models.TextField()  # This field type is a guess.
    minimumorderquantity = models.TextField()  # This field type is a guess.
    price = models.TextField()  # This field type is a guess.
    trial_standardcostprice_28 = models.TextField()  # This field type is a guess.
    productdiscount = models.TextField()  # This field type is a guess.
    trial_allowoperatordiscount_30 = models.BigIntegerField()
    productremarks = models.TextField()
    picture1 = models.TextField()
    picture2 = models.TextField()
    trial_recipecomponents_34 = models.BigIntegerField()
    trial_recorddatetime_35 = models.DateTimeField()
    companyid = models.BigIntegerField()
    trial_sessionid_37 = models.TextField()
    trial_isactive_38 = models.BigIntegerField()
    isfixed = models.BigIntegerField()
    conversionfactor = models.TextField()  # This field type is a guess.
    alternateunitid = models.BigIntegerField()
    trial_changeconversion_42 = models.BigIntegerField()
    itemtype = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='itemtype')
    weighingscaleexport = models.BigIntegerField()
    trial_weighingscaleconversion_45 = models.BigIntegerField()
    trial_printnameother_46 = models.TextField()
    trial_generateproductchild_47 = models.BigIntegerField()
    trial_couponfile_48 = models.TextField()
    spcommpercent = models.TextField()  # This field type is a guess.
    spcommamt = models.TextField()  # This field type is a guess.
    schemeids = models.TextField()
    trial_pmfield1_52 = models.TextField()
    pmfield2 = models.TextField()
    trial_pmfield3_54 = models.TextField()
    pmfield4 = models.TextField()
    trial_pmfield5_56 = models.TextField()
    pmfield6 = models.TextField()
    trial_pmfield7_58 = models.TextField()
    pmfield8 = models.TextField()
    pmfield9 = models.TextField()
    pmfield10 = models.TextField()
    calcnetweight = models.BigIntegerField()
    barcoderatio = models.TextField()  # This field type is a guess.
    link = models.TextField()
    askquantity = models.BigIntegerField()
    askcontainer = models.BigIntegerField()
    serviceitem = models.TextField()
    rate = models.TextField()  # This field type is a guess.
    periodicity = models.BigIntegerField()
    upcean1 = models.TextField(unique=True)
    upcean2 = models.TextField(unique=True)
    trial_upcean3_72 = models.TextField(unique=True)
    upcean4 = models.TextField(unique=True)
    trial_teamid_74 = models.TextField()
    trial_changecontainerweight_75 = models.BigIntegerField()
    trial_saleaccountid_76 = models.BigIntegerField()
    salereturnaccountid = models.BigIntegerField()
    trial_purchaseaccountid_78 = models.BigIntegerField()
    purchasereturnaccountid = models.BigIntegerField()
    taxablevalue = models.TextField()  # This field type is a guess.
    loguser = models.BigIntegerField()
    loglocation = models.BigIntegerField()
    logsession = models.TextField()
    webgroupid = models.BigIntegerField()
    websubgroupid = models.BigIntegerField()
    webitemname = models.TextField()
    trial_isrecommended_87 = models.BigIntegerField()
    foodtype = models.BigIntegerField()
    spicelevel = models.BigIntegerField()
    webproductname = models.TextField()
    convertproductid = models.TextField()
    convertqty = models.TextField()  # This field type is a guess.
    mlnumber = models.BigIntegerField()
    hsnsacid = models.ForeignKey(Hsnsacmaster, models.DO_NOTHING, db_column='hsnsacid', related_name='productmasterhsnsacid')
    productcodesap = models.TextField()
    generateproduction = models.BigIntegerField()
    trial_spcommdatewise_97 = models.TextField()
    sacid = models.ForeignKey(Hsnsacmaster, models.DO_NOTHING, db_column='sacid', related_name='productmastersacid')

    class Meta:
        managed = False
        db_table = 'productmaster'