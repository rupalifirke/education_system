import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from datetime import datetime
                
# get current user's posts
@app.route('/my-posts/<int:student_id>')
def myposts(student_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM post WHERE StudentId=%s", student_id)
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()   
        
        
# Get course by student id
        
@app.route('/get-my-courses/<int:student_id>')
def get_my_courses(student_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM course JOIN enrolled_students ON course.CourseId = enrolled_students.CourseId WHERE enrolled_students.StudentId =%s",student_id) 
        row = cursor.fetchall()
        res = jsonify(row)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()       
      
         
        
# Get post details
@app.route('/post-details/<int:post_id>')
def get_postdetails(post_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM post WHERE PostId=%s", post_id)
        row = cursor.fetchone()
        res = jsonify(row)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()       
     
        
        
# get all recent assignments:
                
@app.route('/get-course-assigns/<int:course_id>')
def get_course_assigns(course_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM exam WHERE CourseId=%s",course_id) 
        row = cursor.fetchall()
        res = jsonify(row)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()    
        
 
# post comment            
@app.route('/post_comment', methods=['POST'])
def post_real_comment():
    try:
        _json = request.json
      #  _post_id = _json['_post_id']
        _post_id = _json['_post_id']
        _stud_id = _json['_stud_id']
        _content = _json['_content']       
        # insert record in database
        sqlQuery = "INSERT INTO comment (PostId, StudentId, Content,created_at) VALUES(%s, %s, %s, %s)"
        data = (_post_id, _stud_id, _content, datetime.now())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        res = jsonify('comment posted successfully.')
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  
    
    
#to delete posts by student       
        
@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM post WHERE PostId=%s",post_id)
        conn.commit()
        print(cursor.rowcount)
        if cursor.rowcount==0:
            res = jsonify('Record Not found.')
            res.status_code = 204
            return res
        res = jsonify('Student deleted successfully.')
        res.status_code = 200
        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()        
        
        
        
    

# create Student            
@app.route('/create', methods=['POST'])
def create_student():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _password = _json['password']

        
        # insert record in database
        sqlQuery = "INSERT INTO student(id, name, email, password) VALUES(%s, %s, %s, %s)"
        data = (_id, _name, _email, _password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        res = jsonify('Student created successfully.')
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
# Get all courses
@app.route('/course')
def course():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM course")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
    
# Get particular students enrolled in specific courses
@app.route('/enrolled_students/<int:course_id>')
def enrolled_students(course_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from student s Where s.Id in (select StudentId from enrolled_students e Where e.CourseId=%s)",(course_id,))
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
        
      
        

# enroll student in a course        
@app.route('/enroll/<int:student_id>/<int:course_id>')
def enroll_student(student_id, course_id):
       
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `enrolled_students` VALUES (%s,%s, null)", (student_id, course_id))
        conn.commit()
        print(cursor.rowcount)
        if cursor.rowcount==0:
            res = jsonify('Record Not found.')
            res.status_code = 204
            return res
        res = jsonify('Student enrolled successfully.')
        res.status_code = 200
        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


# Get all students
@app.route('/student')
def student():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
# Get student by id
@app.route('/student/<int:student_id>')
def id_student(student_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM student WHERE id=%s", student_id)
        row = cursor.fetchone()
        res = jsonify(row)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


# To edit Student Info

@app.route('/update', methods=['PUT'])
def update_student():
     try:
         _json = request.json
        _student_id = _json['id']
         _first_name = _json['first_name']
         _last_name = _json['last_name']
         _class = _json['class']
         _age = _json['age']
         _address = _json['address']

    
        
         # update record in database
         sql = "UPDATE student SET first_name=%s, last_name=%s, class=%s, age=%s, address=%s WHERE id=%s"
         data = (_first_name, _last_name, _class, _age, _address, _student_id,)
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(sql, data)
         conn.commit()
         res = jsonify('Student updated successfully.')
         res.status_code = 200

         return res
     except Exception as e:
         print(e)
     finally:
         cursor.close() 
         conn.close()

# delete student record from database        
@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id=%s", (student_id,))
        conn.commit()
        print(cursor.rowcount)
        if cursor.rowcount==0:
            res = jsonify('Record Not found.')
            res.status_code = 204
            return res
        res = jsonify('Student deleted successfully.')
        res.status_code = 200
        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404

    return res


        
# post comment            
@app.route('/post_doubt', methods=['POST'])
def post_comment():
    try:
        _json = request.json
      #  _post_id = _json['_post_id']
        _stud_id = _json['_stud_id']
        _course_id = _json['_course_id']
        _title = _json['_title']
        _desc = _json['_desc']

        
        # insert record in database
        sqlQuery = "INSERT INTO post (StudentId, CourseId, Title, Description,created_at) VALUES(%s, %s, %s, %s, %s)"
        data = (_stud_id, _course_id, _title, _desc, datetime.now())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        res = jsonify('comment posted successfully.')
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        


# Get comment by id
@app.route('/get_comment/<int:post_id>')
def get_comments_bypost(post_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM comment JOIN student ON comment.StudentId = student.id WHERE comment.PostId=%s", post_id)
        row = cursor.fetchall()
        res = jsonify(row)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route('/student_grade/<int:stud_id>')
def enrolled_students2(stud_id):
   try:
      conn = mysql.connect()
      cursor = conn.cursor(pymysql.cursors.DictCursor)
     #cursor.execute("Select CourseId,sum(Marks_Earned)/Count(Marks_Earned) as perecentage From exam_appears where StudentId=%s Group By CourseId",stud_id)
      cursor.execute("Select e.CourseId,Name,sum(Marks_Earned)/Count(Marks_Earned)  as Score From exam_appears e,course c where c.CourseId=e.CourseId and StudentId=%s Group By e.CourseId",stud_id)
      rows = cursor.fetchall()
      res = jsonify(rows)
      res.status_code = 200

      return res
   except Exception as e:
      print(e)
   finally:
      cursor.close() 
      conn.close()



if __name__ == "__main__":
    app.run()    
