SELECT subject_area 主题,
    workflow_name 工作流名称,
    session_instance_name 会话名,
    mapping_name 映射名,
    successful_source_rows 源成功num,
    failed_source_rows 源失败num,
    successful_rows 目标成功num,
    failed_rows 目标失败num,
    actual_start 执行时间,
    first_error_code 错误代码,
    first_error_msg 错误信息
FROM INFA_REP.rep_sess_log
WHERE TO_CHAR(actual_start,'yyyymmdd') = TO_CHAR(SYSDATE,'yyyymmdd')/*workflow运行时间*/
AND (first_error_code <> 0 OR
        mapping_name IS NULL OR
        failed_rows > 0)
ORDER BY actual_start;