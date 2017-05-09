
(define (deep-map fn s)
  ; YOUR-CODE-HERE
  (cond ((null? s) nil)
   		((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
  		(else (cons (fn (car s)) (deep-map fn (cdr s)))))
)

(define (substitute s old new)
  ; YOUR-CODE-HERE
  (define (replace x) (if (eq? old x) new x))
  (deep-map replace s)
)

(define (deep-map-two fn s olds news)
  ; YOUR-CODE-HERE
  (cond ((null? s) nil)
   		((list? (car s)) (cons (deep-map-two fn (car s) olds news) (deep-map-two fn (cdr s) olds news)))
  		(else (cons (fn (car s) olds news) (deep-map-two fn (cdr s) olds news))))
)
(define (sub-all s olds news)
  ; YOUR-CODE-HERE
  (define (replace x olds news) (cond ((null? olds) x)
					   				((eq? x (car olds)) (car news))
									(else (replace x (cdr olds) (cdr news)))))
  (deep-map-two replace s olds news)
)


