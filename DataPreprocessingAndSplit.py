types=pd.get_dummies(final_data['Type'])
hol=pd.get_dummies(final_data['IsHoliday'])

data= pd.concat([final_data, types],axis=1)
data= pd.concat([data, hol],axis=1)
data.head()
data=data.drop(['Type','IsHoliday'],axis=1)
data.isnull().sum()
target= data['Weekly_Sales']
final=data.drop(['Date','Weekly_Sales'],axis=1)
final=final.drop(['MarkDown1','MarkDown2','MarkDown4','MarkDown5'],axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(final,target,test_size=0.2,random_state=1)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x_train.columns = x_train.columns.astype(str)

# Now you should be able to fit_transform without errors
x = scaler.fit_transform(x_train)

x_test.columns = x_test.columns.astype(str)

# Now transform x_test
test = scaler.transform(x_test)

s=StandardScaler()
y_train=s.fit_transform(np.array(y_train).reshape(-1,1))
y_test=s.transform(np.array(y_test).reshape(-1,1))
