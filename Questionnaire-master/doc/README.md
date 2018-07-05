# 文档

# 说明

## 客户端

**请求方法**

如果客户端不支持:PUT,DELETE,HEAD,OPTIONS方法,需要在请求头中添加`X-Method: method`字段,来表明需要使用的请求方法。

例如：`xhr.setRequestHeader('X-method','put')`

**请求体**

如果客户端需要上传文件，需要在请求头设置`Content-Type: multipart/form-data`。否则全部以json格式上传,并且表明`Content-Type: application/json`。

例如:

提交formdata
```javascript
let xhr=new XMLHttpRequest()
let data=new Formdata()
data.append('name','张三')
data.append('photo',file_input.files[0])
xhr.open('post','/api/v1/user')
xhr.setRequestHeader('X-method','put')
xhr.send(data)
```

提交json

```javascript
let xhr=new XMLHttpRequest()
let data={
    name:"张三",
    age:20
}
xhr.open('post','/api/v1/user')
xhr.setRequestHeader('X-method','put')
xhr.setRequestHeader('Content-Type','application/json')
xhr.send(JSON.stringify(data))
```

## 服务器响应

如果服务器接受了用户请求,那么将会响应

响应头:`HTTP/1.1 200 OK`

响应体:

服务器响应数据内容格式为`application/json`

```json
{
    state: 200,
    msg: 'OK',
    data: {}
}
```
- state: int 状态码
    - 200:成功
    - 401:未登录
    - 403:没有权限
    - 405:方法不支持
    - 422:参数错误
    - 500:服务器发生错误
- msg: string 状态码的说明
- data: json 请求的执行结果

# 接口

## 注册码

### 获取注册码

method: `GET`

body: `none`

path: `/api/v1/regist_code`

response:

```json
{
    state: 200,
    msg: 'OK',
    data: {
        regist_code: 12303
    }
}
```

## 用户

### 获取用户信息

method: GET

path: /api/v1/user

body: none

response:

```json
{
    state: 200,
    msg: 'OK',
    data:{
        user: 1 ,//用户id
        name: '' ,//姓名
        email: '' ,//邮箱
        address: '' ,//地址
        phone: '' ,//固定电话
        mobile: '' ,//手机
        qq: '' ,//qq
        wechat: '' ,//微信
        web: '' ,//网址

        // 以下为公司附带数据
        company: '' ,//公司名称
        industry: '' ,//行业
        description: '' ,//介绍

        // 以下为普通用户接口附带数据
        gender:'', //性别
        birthday:'',//生日 
        job:'',// 职业
        salary:'',//薪酬情况
    }

}
```


### 用户注册

method: `PUT`

path: `/api/v1/user`

body: 
- username: 用户名
- password: 密码
- ensure_password: 确认密码
- regist_code: 注册码
- category: 用户类型 可选['userinfo','customer']

response:

```json
{
    state: 200,
    msg: 'OK',
    data: {
        id: 1 //注册的用户id
    }
}
```

### 更新用户信息

method: `POST`

path: `/api/v1/user`

body: 
- name: 姓名
- email: 邮箱
- address: 地址
- phone: 固定电话
- mobile: 手机
- qq: qq
- wechat: 微信

以下为公司附带数据
- company: 公司名称
- industry: 行业
- description: 介绍
- web: 网址

以下为普通用户接口附带数据
- age: 年龄
- gender: 性别 可选['male','female']
- job:  职业
- salary: 薪酬情况

response:

```json
{
    state: 200,
    msg: 'OK',
    data: {
            'msg': '更新成功'
    }
}
```

## 登录退出

### 获取登录信息

method: `GET`

path: `/api/v1/session`

body: `none`

response:

```json
//已经登录
{
    state: 200,
    msg: 'OK',
    data: {
        'msg': '已经登录'
    }
}
//未登录
{
    state: 401,
    msg: '未登录',
}
```

### 登录

method: `PUT`

path: `/api/v1/session`

body: 
- username:用户名
- password:密码

response:

```json
// 登录成功
{
    state: 200,
    msg: 'OK',
    data: {
        'msg': '登录成功'
    }
}
//登录失败
{
    state: 422,
    msg: '参数错误',
    data: {
        'msg': '用户名或密码错误'
    }
}
```

### 退出

method: `DELETE`

path: `/api/v1/session`

body: `none`

response:

```json
{
    state: 200,
    msg: 'OK',
    data: {
        'msg': '退出成功'
    }
}
```



## 问卷列表

### 管理员获得问卷列表

### 用户获得问卷列表
















