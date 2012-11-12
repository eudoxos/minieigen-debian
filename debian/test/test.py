#! /usr/bin/env python

import unittest, math
import minieigen as mne

class SimpleTests(unittest.TestCase):
  def testVector2i(self):
    a2i = mne.Vector2i(2,1)
    b2i = mne.Vector2i(3,5)
    c2i = a2i + b2i

    self.failUnlessEqual(c2i[0],5)
    self.failUnlessEqual(c2i[1],6)
    
    c2i *= 2
    
    self.failUnlessEqual(c2i[0],10)
    self.failUnlessEqual(c2i[1],12)
    
  def testVector3(self):
    a3r = mne.Vector3(2.1,1.1,4.3)
    b3r = mne.Vector3(3.1,5.1,5.2)
    c3r = a3r + b3r
    
    self.failUnlessAlmostEqual(c3r[0],5.2)
    self.failUnlessAlmostEqual(c3r[1],6.2)
    self.failUnlessAlmostEqual(c3r[2],9.5)
    
    c3r *= 3
    
    self.failUnlessAlmostEqual(c3r[0],15.6)
    self.failUnlessAlmostEqual(c3r[1],18.6)
    self.failUnlessAlmostEqual(c3r[2],28.5)
    
  def testMatrix3Test(self):
    a3m=mne.Matrix3(1,2,3,
                    4,5,6,
                    7,8,9)
    b3m=a3m.transpose()
    self.failUnlessEqual(b3m[0][0],1)
    self.failUnlessEqual(b3m[0][1],4)
    self.failUnlessEqual(b3m[0][2],7)
    self.failUnlessEqual(b3m[1][0],2)
    self.failUnlessEqual(b3m[1][1],5)
    self.failUnlessEqual(b3m[1][2],8)
    self.failUnlessEqual(b3m[2][0],3)
    self.failUnlessEqual(b3m[2][1],6)
    self.failUnlessEqual(b3m[2][2],9)
    
    c3m=a3m.diagonal()
    self.failUnlessEqual(c3m[0],1)
    self.failUnlessEqual(c3m[1],5)
    self.failUnlessEqual(c3m[2],9)
    
    self.failUnlessEqual(a3m.maxAbsCoeff(),9)
    
    
  def testQuaternion(self):
    q1 = mne.Quaternion.Identity
    self.failUnlessEqual(q1[3],1)
    
    q2 = q1.inverse()
    self.failUnlessEqual(q2[3],1)
    
    q3=mne.Quaternion(mne.Vector3(1,0,0),math.pi/2.0)
    m3q=q3.toRotationMatrix()
    self.failUnlessEqual(m3q[0][0],1)
    self.failUnlessEqual(m3q[1][2],-1)
    
    q4=q3.setFromTwoVectors(mne.Vector3(1,2,3),mne.Vector3(2,3,4))
    self.failUnlessEqual(q4.norm(),1)

if __name__ == '__main__':
    unittest.main()
