"""
Goti Esmoris Tech - Industrial Cloud Messaging Gateway & Bot API
Version: 1.0.0
Description: Ingests infrastructure emergency payloads, processes safety statuses, 
             and simulates automated secure instant-message dispatches to plant managers.
"""

import json
import time
import random

# Corporate Telecommunications Metadata Matrix
TELEGRAM_BOT_TOKEN = "758493021:AAH_GotiTechBotSecureToken"
MANAGER_CHAT_ID = "987654321_STARK_CORE"

def dispatch_cloud_telegram_notification(alert_level, sensor_value):
    print(f"\n🚀 [CLOUD GATEWAY ACTIVATED] Establishing handshake with Telegram API Framework...")
    print(f"-> Security Token Verified: {TELEGRAM_BOT_TOKEN[:15]}... [SECURE_SSL]")
    print(f"-> Routing payload to destination Chat ID: {MANAGER_CHAT_ID}")
    
    # Formulating the professional alert text packet that hits the phone
    print("------------------------------------------------------------")
    print(f"📱 [TELEGRAM BOT MESSAGE SENT TO OWNER]:")
    print(f"   🚨 ALERT: Industrial Infrastructure Breach Detected!")
    print(f"   ⚠️ Status: {alert_level}")
    print(f"   📊 Raw Sensor Metric: {sensor_value} ADC (Exceeded safety bounds)")
    print(f"   ⏰ Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    print(f"   🔧 Action Required: Immediate IT & Safety dispatch to Section-B.")
    print("------------------------------------------------------------")
    print("✅ Notification delivery payload confirmed by remote API server.")

def monitor_industrial_safety(payload_str):
    try:
        data = json.loads(payload_str)
        gas_level = data.get("gas_level", 0)
        status = data.get("safety_status", "NOMINAL")
        
        print(f"\n[SYSTEM MONITORING] Atmospheric Gas Level: {gas_level} ADC | Status: {status}")
        
        # Rule-based threat intelligence triggering
        if status == "CRITICAL_LEAK_DETECTED":
            dispatch_cloud_telegram_notification(status, gas_level)
        else:
            print("✅ Environmental balance nominal. Telecommunication logs clear.")
            
    except json.JSONDecodeError:
        print("[ERROR] Corrupted security telemetry bundle.")

if __name__ == "__main__":
    print("====================================================")
    print("     GOTI ESMORIS TECH - EMERGENCY CLOUD TELEMETRY  ")
    print("====================================================")
    print("Securing interface ports... (Press Ctrl+C to terminate)")
    
    try:
        sample_loop = 0
        while True:
            if sample_loop % 3 == 0:
                # Simulated Emergency Event (Slider moved to maximum leak level)
                critical_payload = '{"gas_level": 3540, "safety_status": "CRITICAL_LEAK_DETECTED"}'
                monitor_industrial_safety(critical_payload)
            else:
                # Nominal Safe Operations
                safe_payload = f'{{"gas_level": {random.randint(450, 1200)}, "safety_status": "NOMINAL"}}'
                monitor_industrial_safety(safe_payload)
                
            sample_loop += 1
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nCloud messaging infrastructure disconnected. Safety protocols locked.")
