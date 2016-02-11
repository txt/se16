(defun visitr (things f)
  "visitor patterns in functional programming"
  (if (atom things)
      (funcall f things)   ; then
      (dolist (one things) ; else do for each
	(visitr one f))))

(defun somethingNasty()
  '(a 
    (b 1) 
    c
    (d e 
     (f g 
      (2 2 2)
      )
     h)
    (i j)
    (k
     (l
      (m
       (n o p q r 
	  (s 3 3 3)
	  (t 4 4 )
	  u v w x y z))))))
    
(defun demo1 ()
  (let (all)
    (visitr (somethingNasty)  (lambda (x)
				(and (numberp x)
				     (push x all))))
    all))

(defun demo2 (&optional (most 0))
  (let (uniques)
    (visitr (somethingNasty)  (lambda (x)
				(and (numberp x)
				     (> x most)
				     (not (member x uniques))
				     (push x uniques))))
    uniques))

(print(demo1))

(print (demo2))
(print (demo2 2))


; output
; (9 8 7 6 5 4 3 2 1)

