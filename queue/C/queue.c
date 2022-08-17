#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

typedef struct {
  int item[SIZE];
  int rear, front;
}Queue;

// function prototypes
void initQueue(Queue *);
void enqueue(Queue *, int );
int dequeue(Queue *);

void initQueue(Queue *qp){
  qp -> front = 0;
  qp-> rear = 0;
}

void enqueue(Queue *qp, int v){
  if (qp->rear == SIZE){
    printf("Queue Overflow\n");
    return;
  }
  qp->item[qp->rear] = v;
  qp->rear = qp->rear + 1;
}

int dequeue(Queue *qp){
  if (qp->rear == qp->front){
    return -9999;   //when the queue is empty we will return absurd value
  }
  int v = qp->item[qp->front];
  qp->front = qp->front + 1;
  return v;
}


int main() {
  Queue q;
  initQueue(&q);

  enqueue(&q, 5);
  enqueue(&q, 10);
  enqueue(&q, 15);
  enqueue(&q, 20);

  printf("%d\n", dequeue(&q));
  printf("%d\n", dequeue(&q));
  printf("%d\n", dequeue(&q));
  printf("%d\n", dequeue(&q));

  printf("%d\n", dequeue(&q));

  return 0;
}
