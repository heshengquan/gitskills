# -*- coding:utf-8 -*-
import time
import json


def get_smp_count(start_time, end_time, id):
    # 根据时间和业务系统id获取告警总次数、攻击次数、异常流量总量
    resp = {}

    try:
        asset_key_sql = """
        select asset.asset_key
        from public.tbl_asset_info as asset
        inner join public.tbl_tag_assets as tag
        on asset.uuid = tag.asset_uuid
        where tag.tag_id={} and asset.category=1
        """

        asset_key_sql = asset_key_sql.format(id)
        asset_key_list = json.loads(CFunction.execute(CPgSqlParam(asset_key_sql)))

        asset_key_list = list(item[0] for item in asset_key_list)
        asset_key_tuple = tuple(asset_key_list)

        print asset_key_tuple
        # 异常流量总量
        feat_byte_sum_sql = """
        select sum(feat_bytes)
        from internal_app_bsaata.nta_t_event
        where atk_ip in {} and start_timestamp>={} and end_timestamp<={}
        """

        feat_byte_sum_sql = feat_byte_sum_sql.format(asset_key_tuple, start_time, end_time)
        feat_byte_sum = json.loads(CFunction.execute(CPgSqlParam(feat_byte_sum_sql)))[0][0]

        # 攻击次数是指网络入侵对应的事件数
        attack_count_sql = """
        select count(0)
        from internal_app_bsackc.event
        where dip in {} and start_time>={} and end_time<={}
        """

        attack_count_sql = attack_count_sql.format(asset_key_tuple, start_time, end_time)
        attack_count = json.loads(CFunction.execute(CPgSqlParam(attack_count_sql)))[0][0]

        # 告警次数
        alarm_count_sql = """
        select count(0)
        from internal_app_bsatsa.event
        where dip in {} and start_time>={} and end_time<={}
        """
        alarm_count_sql = alarm_count_sql.format(asset_key_tuple, start_time, end_time)
        alarm_count = json.loads(CFunction.execute(CPgSqlParam(alarm_count_sql)))[0][0]

        resp = {"feat_byte_sum": feat_byte_sum, "attack_count": attack_count, "alarm_count": alarm_count}
        return resp

    except Exception as e:
        raise e.message
