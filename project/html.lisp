(defmacro say (s)
  `(format t "~a~%" ,s))

(defmacro as (tag content)
  `(format nil "<~(~A~)>~A</~(~A~)>"
	   ',tag ,content ',tag))

(defmacro p (x)  `(as "p" ,x))
(defmacro ul (&rest lst)  
   `(progn
      (dolist (one lst) (as "li" one))))

(defmacro with (tag &rest body)
  `(progn
     (format t "~&<~(~A~)>~%" ',tag)
     ,@body
     (format t "~&</~(~A~)>~%" ',tag)))

(defun brs (&optional (n 1))
  (fresh-line)
  (dotimes (i n)
    (princ "<br>"))
  (terpri))


(defun html-file (base)
  (format nil "~(~A~).html" base))

(defmacro page (name title &rest body)
  (let ((ti (gensym)))
    `(with-open-file (*standard-output*
		      (html-file ,name)
		      :direction :output
		      :if-exists :supersede)
		     (let ((,ti ,title))
		       (as title ,ti)
		       (with center
			     (as h2 (string-upcase ,ti)))
		       (brs 3)
		       ,@body))))


(defmacro with-link (dest &rest body)
  `(progn
     (format t "<a href=\"~A\">" (html-file ,dest))
     ,@body
     (princ "</a>")))

(defun link-item (dest text)
  (princ "<li>")
  (with-link dest
	     (princ text)))

(defun button (dest text)
  (princ "[ ")
  (with-link dest
	     (princ text))
  (format t " ]~%"))

(say (as "p" "asdas"))
(say (p "asdas"))
(say (ul "aa" "bbb" "ccc"))

t
