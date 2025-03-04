import gdown

# URL file Google Drive (thay đổi từ dạng "view" sang "uc" để gdown hoạt động)
url = "https://3zfmbk-my.sharepoint.com/personal/xmbll_3zfmbk_onmicrosoft_com/_layouts/15/download.aspx?UniqueId=8d96475c-fac5-4de6-b6c9-6a3a0b6140b7&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2ZmYyZTZkMy1iZmQ0LTRmMDAtYjZkZS0yZDE2NjE1ZTRiYzciLCJhcHBfZGlzcGxheW5hbWUiOiJhbGlzdCIsImFwcGlkIjoiMjIzNTg5MDYtOTI2OS00ZjQzLWIyMzUtMDU3MjU4ZjQ1ZTA0IiwiYXVkIjoiMDAwMDAwMDMtMDAwMC0wZmYxLWNlMDAtMDAwMDAwMDAwMDAwLzN6Zm1iay1teS5zaGFyZXBvaW50LmNvbUAxN2QwODU4Yy04MTliLTQxY2ItODc0My00NDg2ODQyNDViYjIiLCJleHAiOiIxNzM3NDcxNDE4In0.CgoKBHNuaWQSAjY0EgsIwOqAk7CL3T0QBRoOMjAuMTkwLjE0NC4xNzAqLFBBQjJid1pLRUJqelJuaWdROVNuN3lxVkU1ZEtFQ1QycUJ1VGNWZzlObUk9MJ4BOAFCEKF5tTyRIABAUldpyp073lpKEGhhc2hlZHByb29mdG9rZW5SCFsia21zaSJdcikwaC5mfG1lbWJlcnNoaXB8MTAwMzIwMDI0NzNiMTc4NEBsaXZlLmNvbXoBMoIBEgmMhdAXm4HLQRGHQ0SGhCRbspIBBmJvbGFuZ5oBAmRhogEceG1ibGxAM3pmbWJrLm9ubWljcm9zb2Z0LmNvbaoBEDEwMDMyMDAyNDczQjE3ODSyAQ5hbGxmaWxlcy53cml0ZcgBAQ.06JAgyvYE2LDtCXSenUgHbRIdKzDIGNAEllrPADsY4g&ApiVersion=2.0"

# Đường dẫn lưu file sau khi tải
output = "/mnt/a.qcow2"  # Đường dẫn đầy đủ nơi lưu file

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
