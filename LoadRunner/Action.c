Action()
{


	lr_rendezvous("login");/*���ϵ�*/

	web_reg_find("Text=\"code\": 200,",/*���㣨���ԣ�*/
		LAST);

	web_reg_save_param("token1",/*��������*/
		"LB=\"token\": \"",
		"RB=\"",
		LAST);

	lr_start_transaction("��¼");

	web_custom_request("web_custom_request",
		"URL=http://132.232.44.158:5000/userLogin/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"{account}\", \"password\":\"{password}\", \"captcha\":\"123456\"}",
		LAST);

	lr_end_transaction("��¼", LR_AUTO);

	//lr_think_time(5);


	lr_start_transaction("�û��ظ���Ϣ");

	web_reg_find("Text=\"code\": 200,",
		LAST);

	web_custom_request("web_custom_request",
		"URL=http://132.232.44.158:5000/articleComment/",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":1, \"content\":\"lalalalala\",\"token\": \"{token1}\"}",/*����token1����*/
		LAST);

	lr_end_transaction("�û��ظ���Ϣ", LR_AUTO);

	return 0;
}
