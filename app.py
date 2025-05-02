from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
import pygsheets
import os
import logging
from datetime import datetime

# 設定日誌
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 使用隨機生成的密鑰

def init_google_sheets():
    """初始化並連接 Google Sheets"""
    try:
        # 確保憑證文件存在
        creds_path = 'C:/Users/C14511/google-sheets-web/credentials.json'
        if not os.path.exists(creds_path):
            logger.error(f"找不到憑證文件: {creds_path}")
            return None

        # 授權並連接
        gc = pygsheets.authorize(service_file=creds_path)
        logger.info("Google Sheets 授權成功")

        # 開啟試算表
        sheet_url = 'https://docs.google.com/spreadsheets/d/1F6xJwoI-nrWmEsV3eu0AUpb3tcjFQv44d4tZ3DJ1VKg'
        spreadsheet = gc.open_by_url(sheet_url)
        worksheet = spreadsheet.sheet1
        
        # 測試寫入權限
        test_cell = 'A1'
        current_value = worksheet.get_value(test_cell)
        logger.info(f"成功讀取儲存格 {test_cell}: {current_value}")
        
        return worksheet

    except pygsheets.exceptions.AuthenticationError as e:
        logger.error(f"認證錯誤: {str(e)}")
        return None
    except pygsheets.exceptions.SpreadsheetNotFound as e:
        logger.error(f"找不到試算表: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"連接 Google Sheets 時發生錯誤: {str(e)}")
        return None

@app.route('/')
def index():
    """首頁路由"""
    return render_template('Gemini_index.html')

@app.route('/get_qa_list')
def get_qa_list():
    """獲取問答列表路由"""
    try:
        worksheet = init_google_sheets()
        if worksheet is None:
            return jsonify([])  # 回傳空列表

        # 獲取問答記錄
        all_values = worksheet.get_all_values()
        records = []
        for row in all_values:
            question = row[0]
            answer = row[1] if len(row) > 1 else None
            if answer:  # 如果有答案，才顯示該問題
                records.append({'question': question, 'answer': answer, 'timestamp': row[2]})

        return jsonify(records)  # 回傳問答記錄清單

    except Exception as e:
        logger.error(f"獲取問答記錄時發生錯誤: {str(e)}")
        return jsonify([])  # 回傳空列表

@app.route('/submit', methods=['POST'])
def submit_question():
    try:
        worksheet = init_google_sheets()
        if worksheet is None:
            flash("無法連接 Google Sheets，請稍後再試", "error")
            return redirect(url_for('index'))

        # 獲取並驗證問題
        question = request.form.get('question', '').strip()
        if not question:
            flash("問題不能為空", "error")
            return redirect(url_for('index'))

        # 準備要寫入的資料
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_row = [question, '', timestamp]  # 問題在A列、答案留空、時間戳記在C列

        # 找到第一个空行
        for i in range(1, 1000): 
            cell_value = worksheet.get_value(f'A{i}')
            if not cell_value: 
                next_row = i
                break

        # 如果所有行都已填满，则添加新行
        if 'next_row' not in locals():
            next_row = len(worksheet.get_all_values()) + 1

        # 寫入資料：問題寫入 A 列，答案寫入 B 列
        worksheet.update_row(next_row, new_row)
        logger.info(f"成功將問題寫入第 {next_row} 行: {question}")

        flash("問題已成功提交！", "success")
        return redirect(url_for('index'))

    except Exception as e:
        logger.exception(f"提交問題時發生錯誤: {str(e)}") # 使用 logger.exception 紀錄更詳細的錯誤訊息
        flash("提交問題時發生錯誤，請稍後再試", "error")
        return redirect(url_for('index'))

@app.route('/delete_all_qa', methods=['POST'])
def delete_all_qa():
    """刪除所有問答路由"""
    try:
        worksheet = init_google_sheets()
        if worksheet is None:
            return jsonify({'success': False, 'error': '無法連接 Google Sheets'})
        # 獲取試算表的維度
        rows, cols = worksheet.rows, worksheet.cols
        
        # 清空試算表所有資料，包含標題列
        worksheet.clear(start='A1', end=f'{chr(ord("A") + cols-1)}{rows}') #A1 到最後一個儲存格

        return jsonify({'success': True})

    except Exception as e:
        logger.error(f"刪除所有問答時發生錯誤: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # 確保日誌目錄存在
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # 添加檔案處理程序
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    
    app.run(debug=True, port=5000)