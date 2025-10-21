import psycopg2

conn = psycopg2.connect("dbname=prgpt user=postgres password=yourpass")
cur = conn.cursor()
cur.execute("""
  INSERT INTO pr_metadata (pr_id, summary, review_bullets, comment)
  VALUES (%s, %s, %s, %s)
""", (1, 'Initial PR', '["Check syntax", "Review tests", "Optimize code"]', 'Looks good!'))
conn.commit()
cur.close()
conn.close()