; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (map f s)
  ; List the result of applying f to each element in s.
  (cond ((null? s) s)
   		((number? s) (f s))
    	(else (cons (f (car s)) (map f (cdr s))))))

(define (filter f s)
  ; List the elements of s for which f returns a true value.
  (cond ((null? s) s)
   		((boolean? s) (f s))
		(else (let ((rest (filter f (cdr s))))
      		(if (f (car s)) (cons (car s) rest) rest)))))

(define (no-repeats s)
  ; YOUR-CODE-HERE
  (define (equal x) (= (car s) x))
  (cond ((equal? s nil) nil)
   		((equal? (filter wrong (map equal (cdr s))) nil) (cons (car s) (no-repeats (cdr s))))
		(else (no-repeats (cdr s))))
  )
(define (wrong x) (if (equal? #t x) #t #f))

(define (dot x) (cond 	((number? x) #f)
				 		((number? (cdr x)) #t)
						((pair? (cdr x)) (dot (cdr x)))
						(else #f)))

(define (len x) (cond ((boolean? x) 1)
				 		((null? x) 0)
				 		(else (+ 1 (len (cdr x))))))

(define (how-many-dots s)
  ; YOUR-CODE-HERE
  (len (filter wrong (map dot s)))
)
