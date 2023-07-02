print('Hello World!')
lis = [2, 5, 7, 8, 12]
for i in lis:
    if i % 2 == 0:
        print('the number is even')
    else:
        print('the number is odd')


def say_hello():
    print('hello!')

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set2.issuperset(set1)
set1.issuperset(set2)

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2

import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')

def func(age):
    if age < 30:
        return 1
    else:
        return 0

df['age2'] = df['age'].apply(lambda age: func(age))

df.loc[(df['age'] < 30), 'new_age'] = 1
df.loc[(df['age'] > 30), 'new_age'] = 0

df['new_age'] = df['age'].apply(lambda x: 1 if x < 30 else 0)

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes != 'O']
df.columns
df.nunique()

print("Hello AI Era")

def func(dataframe, var):
    print(f"{var}")
    print(dataframe[var].value_counts())

func(df, 'sex')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def cat_summary(dataframe, col_name, plot=False):  # plot un ön tanımlı değerini false yaptık
   print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                       "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
   print("#####################################################")

def grab_col_names(dataframe, cat_th=10, car_th=20):
   """
   Veri setindeki kategorik, nümerik, ve kategorik fakat kardinal tipte değişkenlerin isimlerini verir.
   Parameters
   ----------
   dataframe: dataframe
      değişken ismi alınmak istenen dataframe'dir.
   cat_th: int, float
       numeric fakat kategorik olan değişkenler için sınıf eşik değeri
   car_th: int, float
       kategorik fakat kardinal değişkenler için sınıf eşik değeri

   Returns
   -------
    cat_cols: list
       kategorik değişken listesi
    num_cols: list
       numerik değişken listesi
    cat_but_car: list
       kategorik görünümlü kardinal değişken listesi

    Notes
    ________
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols un içerisindedir.
   """

#kategorik değişkenler için yaptığımız seçim işlemlerini getirelim
   cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
   num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ["int64", "float64"]]
   cat_but_car = [col for col in df.columns if df[col].nunique() > car_th and str(df[col].dtype) in ["category", "object"]]
   cat_cols = cat_cols + num_but_cat
   cat_cols = [col for col in cat_cols if col not in cat_but_car]
   ############################################################################
   #numerik değişkenler için yaptığımız seçim islemini getirelim

   num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
   num_cols = [col for col in num_cols if col not in cat_cols]
   #########################################################################
   # bu fonksiyona bir de raporlama işlemi ekleyelim
   print(f"Observations: {dataframe.shape[0]}")
   print(f"Observations: {dataframe.shape[1]}")
   print(f"cat_cols: {len(cat_cols)}")
   print(f"num_cols: {len(num_cols)}")
   print(f"cat_but_car: {len(cat_but_car)}")
   print(f"num_but_cat: {len(num_but_cat)}")
   return cat_cols, num_cols, cat_but_car

#bu çıktıları tutmak istiyoruz
cat_cols, num_cols, cat_but_car = grab_col_names(df)

# AMACIMIZ HEDEF DEĞİŞKENİ ANALİZ EDELİM
df["survived"].value_counts()
cat_summary(df, "survived")

# TITANIC VERİ SETİMİZİN HEDEF(TARGET) DEĞİŞKENİ HAYATTA KALMAYI İFADE EDEN SURVİVED DEĞİŞKENİDİR. İNSANLARIN HAYATTA KALMA DURUMLARINI ETKİLEYEN ETKENLERİ ARAŞTIRMANIN YOLU BU DEĞİŞKENİ TEK BAŞINA İNCELEMEK DEĞİLDİR. DEĞİŞKENLERİ ÇAPRAZLAMALIYIZ. YANİ BAĞIMLI DEĞİŞKENE GÖRE DİĞER DEĞİŞKENLERİ GÖZ ÖNÜNDE BULUNDURARAK ANALİZLER YAPMALIYIZ.

# HEDEF DEĞİŞKENİN KATEGORİK DEĞİŞKENLER İLE ANALİZİ

df.groupby("sex")["survived"].mean() # cinsiyete göre groupby'a al ve surviived ın ortalamasına bak

def target_summary_with_cat(dataframe, target, categorical_col):
   print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")

target_summary_with_cat(df, "survived", "sex")

#elimizde bir kategorik değişken listesi olduğu için hepsini gezebilir ve target ımızı seri bir şekilde değerlendirebiliriz.
for col in cat_cols:
   target_summary_with_cat(df, "survived", col)

# HEDEF DEĞİŞKENİN SAYISAL DEĞİŞKENLER İLE ANALİZİ
# kategorik değişkenlerde yaptığımız işlemden farklı olarak bu kez groupby a bağımlı değişkenimizi alarak aggregation bölümüne ise sayısal değişkenimizi alarak ortalamasını alacağız.
df.groupby("survived")["age"].mean()
df.groupby("survived").agg({"age": "mean"})

def target_summary_with_num(dataframe, target, numerical_col):
   print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

target_summary_with_num(df, "survived", "age")

for col in num_cols:
   target_summary_with_num(df, "survived", col)
