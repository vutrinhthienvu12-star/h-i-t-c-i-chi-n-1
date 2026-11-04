from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# ==========================================
# 1. API ĐĂNG NHẬP (Map với BoxLogin & SdkRieng.dll)
# ==========================================
@app.route('/api/auth/login', methods=['POST', 'GET'])
def game_login():
    # Client sẽ gửi Username/Password hoặc GosuId lên đây
    return jsonify({
        "status": 1,
        "message": "success",
        "data": {
            "access_token": "htht_bypass_token_2026",
            "account_id": "888888",
            "is_new_user": False
        }
    })

# ==========================================
# 2. API DANH SÁCH MÁY CHỦ (Map với BoxServers & ServerInfo)
# Tham chiếu dump.cs: BoxServers.SetListServer(List<ServerInfo> lstGameServer, bool showNewServerFirst)
# ==========================================
@app.route('/api/server/list', methods=['POST', 'GET'])
def get_server_list():
    return jsonify({
        "status": 1,
        "data": {
            "servers": [
                {
                    "server_id": 1,             # Map: ServerInfo.m_ServerId
                    "server_name": "S1-Local",  # Map: ServerInfo.m_ServerName
                    "status": 1,                # Map: ServerInfo.m_Status (1 = Bình thường)
                    "is_new": True              # Map: Cờ showNewServerFirst / m_GoTagNew
                }
            ],
            "last_login_server": 1
        }
    })

# ==========================================
# 3. API THÔNG TIN NHÂN VẬT & SẢNH (Map với ArenaPlayer & PlayerInfoData)
# Tham chiếu dump.cs: class ArenaPlayer (m_Level, m_Playername, m_Power, m_Avatar...)
# ==========================================
@app.route('/api/user/info', methods=['POST', 'GET'])
def get_user_info():
    return jsonify({
        "status": 1,
        "data": {
            "user_id": 888888,                 # Map: m_UserId
            "player_name": "ThuyenTruong01",   # Map: m_Playername
            "level": 100,                      # Map: m_Level
            "vip_level": 15,                   
            "avatar": 1,                       # Map: m_Avatar (ID ảnh đại diện gốc)
            "type_avatar": 1,                  # Map: m_TypeAvatar
            "power": 9999999,                  # Map: m_Power (Lực chiến)
            "guild_name": "HaiTacLocal",       # Map: m_GuildName
            "server_id": 1,                    # Map: m_ServerId
            
            # Tham chiếu BonusModel (Dữ liệu tiền tệ cơ bản)
            # BONUS_GOLD = 1, BONUS_GEM = 2, BONUS_EXP = 4 (Dump dòng 1520-1522)
            "currencies": {
                "1": 99999999,  # Vàng (BONUS_GOLD)
                "2": 99999999   # Kim Cương (BONUS_GEM)
            }
        }
    })

# ==========================================
# 4. API TẢI TÀI NGUYÊN (Map với AssetBundleManager)
# Tham chiếu dump.cs: AssetBundleManager.SetListAssetBundleInfo(List<AssetInfo> lstAssetInfo)
# ==========================================
@app.route('/api/asset/check_version', methods=['POST', 'GET'])
def check_asset_version():
    # Bắt buộc trả về mảng rỗng hoặc version khớp để Client không đòi tải thêm file từ CDN của Gosu
    return jsonify({
        "status": 1,
        "data": {
            "version": "1.18.0",
            "assets": [] # Truyền mảng rỗng để chặn tải update
        }
    })

# ==========================================
# 5. CATCH-ALL ROUTE (BỘ DÒ TÌM API BÍ MẬT)
# ==========================================
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST', 'GET'])
def catch_all(path):
    # Khúc này CỰC KỲ QUAN TRỌNG. Bất cứ khi nào Client gọi 1 link lạ mà ta chưa viết
    # Nó sẽ chui vào đây. Ông mở Log trên Vercel lên là tóm gọn được ngay tên API đó!
    print(f"[CẢNH BÁO] Client vừa gọi API ẩn: /{path}")
    
    # In luôn data Client gửi lên (để phân tích cấu trúc body)
    if request.is_json:
        print("Data gửi kèm (JSON):", request.json)
    else:
        print("Data gửi kèm (Raw):", request.get_data())

    # Trả về status 1 để lừa Client không bị văng game
    return jsonify({"status": 1, "message": "Bypass Catcher"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
