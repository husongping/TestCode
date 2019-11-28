Action()
{


	lr_rendezvous("login");/*集合点*/

	web_reg_find("Text=\"code\": 200,",/*检查点（断言）*/
		LAST);

	web_reg_save_param("token1",/*关联函数*/
		"LB=\"token\": \"",
		"RB=\"",
		LAST);

	lr_start_transaction("登录");

	web_custom_request("web_custom_request",
		"URL=http://132.232.44.158:5000/userLogin/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"{account}\", \"password\":\"{password}\", \"captcha\":\"123456\"}",
		LAST);

	lr_end_transaction("登录", LR_AUTO);

	//lr_think_time(5);


	lr_start_transaction("用户回复消息");

	web_reg_find("Text=\"code\": 200,",
		LAST);

	web_custom_request("web_custom_request",
		"URL=http://132.232.44.158:5000/articleComment/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":1, \"content\":\"lalalalala\",\"token\": \"{token1}\"}",/*引用token1参数*/
		LAST);

	lr_end_transaction("用户回复消息", LR_AUTO);

	return 0;
}
