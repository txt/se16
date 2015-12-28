(defun visitr (things f)
  "visitor patterns in functional programming"
  (if (atom things)
      (funcall f things)   ; then
      (dolist (one things) ; else do for each
	(visitr one f))))

(defun demo (&aux all)
  (let ((nastyComplexThing
	 '(a 
	   (b 1) 
	   c
	   (d e 
	      (f g 
		 (2 3 4)
		 )
	      h)
	   (i j)
	   (k
	    (l
	     (m
	      (n o p q r 
		 (s 5 6 7)
		 (t 8 9 )
		 u v w x y z)))))))
    (visitr nastyComplexThing
	    (lambda (x)
	      (if (numberp x)
		  (push x all))))
    all))

(print(demo))

; output
; (9 8 7 6 5 4 3 2 1)

