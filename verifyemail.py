'''
在线验证邮箱真实性
'''

import random
import smtplib
import logging

import dns.resolver

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger()


def fetch_mx(host):
    '''
    解析服务邮箱
    :param host:
    :return:
    '''
    logger.info('正在查找邮箱服务器')
    answers = dns.resolver.query(host, 'MX')
    res = [str(rdata.exchange)[:-1] for rdata in answers]
    logger.info('查找结果为：%s' % res)
    return res


def verify_istrue(email):
    '''
    :param email:
    :return:
    '''
    email_list = []
    email_obj = {}
    final_res = {}
    if isinstance(email, str) or isinstance(email, bytes):
        email_list.append(email)
    else:
        email_list = email

    for em in email_list:
        name, host = em.split('@')
        if email_obj.get(host):
            email_obj[host].append(em)
        else:
            email_obj[host] = [em]

    for key in email_obj.keys():
        host = random.choice(fetch_mx(key))
        logger.info('正在连接服务器...：%s' % host)
        s = smtplib.SMTP(host)
        for need_verify in email_obj[key]:
            helo = s.docmd('HELO zheshiwoQQ190758586.cn')
            logger.debug(helo)

            send_from = s.docmd('MAIL FROM:<3123@tengtengml.xyz>')
            logger.debug(send_from)

            send_from = s.docmd('RCPT TO:<%s>' % need_verify)
            logger.debug(send_from)
            final_res[need_verify] = True if send_from[0] == 250 else False
        s.close()

    return final_res


if __name__ == '__main__':
    final_list = verify_istrue(['190758586@qq.com', '19075858666@qq.com'])
    print(final_list)
