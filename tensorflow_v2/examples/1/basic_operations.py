from __future__ import print_function
import tensorflow as tf

#定义张量
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(5)
#一些张量运算
add = tf.add(a,b)
sub = tf.subtract(a,b)
mul = tf.multiply(a,b)
div = tf.divide(a,b)

#计算结果
print("add =",add.numpy())
print("sub = ",sub.numpy())
print("mul =", mul.numpy())
print("div =", div.numpy())
