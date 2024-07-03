from typing import Dict
from pydantic import BaseModel, Field


class Connection(BaseModel):
    mqtt_state: str = Field(..., description="MQTT connection state.")
    prov_state: str = Field(..., description="Provision state.")
    auth_state: str = Field(..., description="Authentication state.")
    sc_stream: str = Field(..., description="SC stream status.")
    sc_debug: str = Field(..., description="SC debug status.")


class PV(BaseModel):
    agg_p_mw: int = Field(..., description="Aggregated PV power in MW.")
    agg_s_mva: int = Field(..., description="Aggregated PV apparent power in MVA.")
    agg_p_ph_a_mw: int = Field(..., description="Aggregated PV phase A power in MW.")
    agg_p_ph_b_mw: int = Field(..., description="Aggregated PV phase B power in MW.")
    agg_p_ph_c_mw: int = Field(..., description="Aggregated PV phase C power in MW.")
    agg_s_ph_a_mva: int = Field(..., description="Aggregated PV phase A apparent power in MVA.")
    agg_s_ph_b_mva: int = Field(..., description="Aggregated PV phase B apparent power in MVA.")
    agg_s_ph_c_mva: int = Field(..., description="Aggregated PV phase C apparent power in MVA.")


class Storage(BaseModel):
    agg_p_mw: int = Field(..., description="Aggregated storage power in MW.")
    agg_s_mva: int = Field(..., description="Aggregated storage apparent power in MVA.")
    agg_p_ph_a_mw: int = Field(..., description="Aggregated storage phase A power in MW.")
    agg_p_ph_b_mw: int = Field(..., description="Aggregated storage phase B power in MW.")
    agg_p_ph_c_mw: int = Field(..., description="Aggregated storage phase C power in MW.")
    agg_s_ph_a_mva: int = Field(..., description="Aggregated storage phase A apparent power in MVA.")
    agg_s_ph_b_mva: int = Field(..., description="Aggregated storage phase B apparent power in MVA.")
    agg_s_ph_c_mva: int = Field(..., description="Aggregated storage phase C apparent power in MVA.")


class Grid(BaseModel):
    agg_p_mw: int = Field(..., description="Aggregated grid power in MW.")
    agg_s_mva: int = Field(..., description="Aggregated grid apparent power in MVA.")
    agg_p_ph_a_mw: int = Field(..., description="Aggregated grid phase A power in MW.")
    agg_p_ph_b_mw: int = Field(..., description="Aggregated grid phase B power in MW.")
    agg_p_ph_c_mw: int = Field(..., description="Aggregated grid phase C power in MW.")
    agg_s_ph_a_mva: int = Field(..., description="Aggregated grid phase A apparent power in MVA.")
    agg_s_ph_b_mva: int = Field(..., description="Aggregated grid phase B apparent power in MVA.")
    agg_s_ph_c_mva: int = Field(..., description="Aggregated grid phase C apparent power in MVA.")


class Load(BaseModel):
    agg_p_mw: int = Field(..., description="Aggregated load power in MW.")
    agg_s_mva: int = Field(..., description="Aggregated load apparent power in MVA.")
    agg_p_ph_a_mw: int = Field(..., description="Aggregated load phase A power in MW.")
    agg_p_ph_b_mw: int = Field(..., description="Aggregated load phase B power in MW.")
    agg_p_ph_c_mw: int = Field(..., description="Aggregated load phase C power in MW.")
    agg_s_ph_a_mva: int = Field(..., description="Aggregated load phase A apparent power in MVA.")
    agg_s_ph_b_mva: int = Field(..., description="Aggregated load phase B apparent power in MVA.")
    agg_s_ph_c_mva: int = Field(..., description="Aggregated load phase C apparent power in MVA.")


class Generator(BaseModel):
    agg_p_mw: int = Field(..., description="Aggregated generator power in MW.")
    agg_s_mva: int = Field(..., description="Aggregated generator apparent power in MVA.")
    agg_p_ph_a_mw: int = Field(..., description="Aggregated generator phase A power in MW.")
    agg_p_ph_b_mw: int = Field(..., description="Aggregated generator phase B power in MW.")
    agg_p_ph_c_mw: int = Field(..., description="Aggregated generator phase C power in MW.")
    agg_s_ph_a_mva: int = Field(..., description="Aggregated generator phase A apparent power in MVA.")
    agg_s_ph_b_mva: int = Field(..., description="Aggregated generator phase B apparent power in MVA.")
    agg_s_ph_c_mva: int = Field(..., description="Aggregated generator phase C apparent power in MVA.")


class Meters(BaseModel):
    last_update: int = Field(..., description="Timestamp of the last update.")
    soc: int = Field(..., description="State of charge.")
    main_relay_state: int = Field(..., description="Main relay state.")
    gen_relay_state: int = Field(..., description="Generator relay state.")
    backup_bat_mode: int = Field(..., description="Backup battery mode.")
    backup_soc: int = Field(..., description="Backup state of charge.")
    is_split_phase: int = Field(..., description="Indicates if the system is split phase.")
    phase_count: int = Field(..., description="Number of phases.")
    enc_agg_soc: int = Field(..., description="Enc aggregated state of charge.")
    enc_agg_energy: int = Field(..., description="Enc aggregated energy.")
    acb_agg_soc: int = Field(..., description="ACB aggregated state of charge.")
    acb_agg_energy: int = Field(..., description="ACB aggregated energy.")
    pv: PV = Field(..., description="PV data.")
    storage: Storage = Field(..., description="Storage data.")
    grid: Grid = Field(..., description="Grid data.")
    load: Load = Field(..., description="Load data.")
    generator: Generator = Field(..., description="Generator data.")


class Tasks(BaseModel):
    task_id: int = Field(..., description="ID of the task.")
    timestamp: int = Field(..., description="Timestamp of the task.")


class DryContact(BaseModel):
    dry_contact_id: str = Field(..., description="ID of the dry contact.")
    dry_contact_type: str = Field(..., description="Type of the dry contact.")
    dry_contact_load_name: str = Field(..., description="Load name of the dry contact.")
    dry_contact_status: int = Field(..., description="Status of the dry contact.")


class Counters(BaseModel):
    main_CfgLoad: int = Field(..., description="Main config load count.")
    main_CfgChanged: int = Field(..., description="Main config change count.")
    main_taskUpdate: int = Field(..., description="Main task update count.")
    MqttClient_publish: int = Field(..., description="MQTT client publish count.")
    MqttClient_respond: int = Field(..., description="MQTT client respond count.")
    MqttClient_msgarrvd: int = Field(..., description="MQTT client message arrived count.")
    MqttClient_create: int = Field(..., description="MQTT client create count.")
    MqttClient_setCallbacks: int = Field(..., description="MQTT client set callbacks count.")
    MqttClient_connect: int = Field(..., description="MQTT client connect count.")
    MqttClient_connect_err: int = Field(..., description="MQTT client connect error count.")
    MqttClient_connect_Err: int = Field(..., description="MQTT client connect Err count.")
    MqttClient_subscribe: int = Field(..., description="MQTT client subscribe count.")
    SSL_Keys_Create: int = Field(..., description="SSL keys create count.")
    sc_hdlDataPub: int = Field(..., description="SC handle data publish count.")
    sc_SendStreamCtrl: int = Field(..., description="SC send stream control count.")
    sc_SendDemandRspCtrl: int = Field(..., description="SC send demand response control count.")
    rest_Status: int = Field(..., description="Rest status count.")


class SystemStatus(BaseModel):
    connection: Connection = Field(..., description="Connection status.")
    meters: Meters = Field(..., description="Meters status.")
    tasks: Tasks = Field(..., description="Tasks information.")
    counters: Counters = Field(..., description="Counters statistics.")
    dry_contacts: Dict[str, DryContact] = Field(..., description="Dry contacts information.")


example_data = {
    "connection": {
        "mqtt_state": "connected",
        "prov_state": "configured",
        "auth_state": "ok",
        "sc_stream": "disabled",
        "sc_debug": "disabled",
    },
    "meters": {
        "timestamp": 1720024407,
        "soc": 0,
        "main_relay_state": 1,
        "gen_relay_state": 5,
        "backup_bat_mode": 1,
        "backup_soc": 30,
        "is_split_phase": 1,
        "phase_count": 0,
        "enc_agg_soc": 0,
        "enc_agg_energy": 0,
        "acb_agg_soc": 0,
        "acb_agg_energy": 0,
        "pv": {
            "agg_p_mw": 0,
            "agg_s_mva": 400000,
            "agg_p_ph_a_mw": 0,
            "agg_p_ph_b_mw": 0,
            "agg_p_ph_c_mw": 0,
            "agg_s_ph_a_mva": 400000,
            "agg_s_ph_b_mva": 0,
            "agg_s_ph_c_mva": 0,
        },
        "storage": {
            "agg_p_mw": 0,
            "agg_s_mva": 0,
            "agg_p_ph_a_mw": 0,
            "agg_p_ph_b_mw": 0,
            "agg_p_ph_c_mw": 0,
            "agg_s_ph_a_mva": 0,
            "agg_s_ph_b_mva": 0,
            "agg_s_ph_c_mva": 0,
        },
        "grid": {
            "agg_p_mw": 1512345,
            "agg_s_mva": 1234567,
            "agg_p_ph_a_mw": 1512345,
            "agg_p_ph_b_mw": 0,
            "agg_p_ph_c_mw": 0,
            "agg_s_ph_a_mva": 1234567,
            "agg_s_ph_b_mva": 0,
            "agg_s_ph_c_mva": 0,
        },
        "load": {
            "agg_p_mw": 1512345,
            "agg_s_mva": 1234567,
            "agg_p_ph_a_mw": 1512345,
            "agg_p_ph_b_mw": 0,
            "agg_p_ph_c_mw": 0,
            "agg_s_ph_a_mva": 1234567,
            "agg_s_ph_b_mva": 0,
            "agg_s_ph_c_mva": 0,
        },
        "generator": {
            "agg_p_mw": 0,
            "agg_s_mva": 0,
            "agg_p_ph_a_mw": 0,
            "agg_p_ph_b_mw": 0,
            "agg_p_ph_c_mw": 0,
            "agg_s_ph_a_mva": 0,
            "agg_s_ph_b_mva": 0,
            "agg_s_ph_c_mva": 0,
        },
    },
    "tasks": {
        "task_id": 123456789,
        "timestamp": 1720024407,
    },
    "counters": {
        "main_CfgLoad": 1,
        "main_CfgChanged": 1,
        "main_taskUpdate": 1,
        "MqttClient_publish": 1234,
        "MqttClient_respond": 20,
        "MqttClient_msgarrvd": 10,
        "MqttClient_create": 25,
        "MqttClient_setCallbacks": 25,
        "MqttClient_connect": 25,
        "MqttClient_connect_err": 15,
        "MqttClient_connect_Err": 15,
        "MqttClient_subscribe": 10,
        "SSL_Keys_Create": 1234,
        "sc_hdlDataPub": 1234,
        "sc_SendStreamCtrl": 123,
        "sc_SendDemandRspCtrl": 1,
        "rest_Status": 1234,
    },
    "dry_contacts": {
        "": {
            "dry_contact_id": "",
            "dry_contact_type": "",
            "dry_contact_load_name": "\u0006",
            "dry_contact_status": 12345678,
        },
        "": {
            "dry_contact_id": "",
            "dry_contact_type": "",
            "dry_contact_load_name": "",
            "dry_contact_status": 12345678,
        },
        "": {
            "dry_contact_id": "",
            "dry_contact_type": "",
            "dry_contact_load_name": "",
            "dry_contact_status": 12345678,
        },
        "": {
            "dry_contact_id": "",
            "dry_contact_type": "",
            "dry_contact_load_name": "",
            "dry_contact_status": 12345678,
        },
    },
}

reports = SystemStatus(**example_data)

for key, value in reports.model_dump().items():
    print(key, value, "\n")
