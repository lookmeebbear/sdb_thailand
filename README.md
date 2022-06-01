# Satellite Derived Bathymetry with IceSAT-2 LiDAR Data : Case Study in the coast of Thailand
การศึกษาการทำแบบจำลองความลึกท้องน้ำตื้น (SATELLITE DERIVED BATHYMETRY) โดยใช้ภาพถ่ายดาวเทียมและค่าระดับจากไลดาร์บนดาวเทียม กรณีศึกษาพื้นที่ชายฝั่งทะเลประเทศไทย 
โครงงานทางวิศวกรรมประจำปีการศึกษา 2564 ของนายเทพชัย ศรีน้อย และ รศ.ดร.ไพศาล สันติธรรมนนท์ ภาควิชาวิศวกรรมสำรวจ คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย 

![Screenshot (419)](https://user-images.githubusercontent.com/88705136/171320963-0ac44fd4-2d7f-4b20-82e5-cd66bb4cf946.png)

ศึกษาการทำแบบจำลองความลึกท้องน้ำตื้น (Bathymetry Model) บริเวณชายฝั่งทะเลประเทศไทย จากภาพถ่ายดาวเทียม Sentinel-2 และค่าระดับจากระบบไลดาร์บนดาวเทียม ICESat-2 ผ่านการเขียน python programming จัดการข้อมูลและทำแบบจำลอง โดยนำเข้าข้อมูลภาพถ่ายจากระบบ Google Earth Engine

ความลึกตัวอย่างทำได้จากการคัดเลือกค่าระดับท้องน้ำและผิวน้ำจาก point cloud จาก ATLAS LiDAR บนดาวเทียม ICESat-2 นำข้อมูลดิบมานำเข้า pandas dataframe หากโหลดข้อมูลเริ่มต้นแบบ hdf5 file นำเข้า python ด้วย library h5py แล้วนำเข้า dataframe เพื่อความสะดวกในการจัดการ

ประเด็นที่สนใจคือเรื่องอัลกอริทึมทำแบบจำลอง (Stumpf or Lyzenga Algorithm) กับ แนวทางการตรวจแก้ภาพ (Sun Glint or Dark Object Subtraction Atmospheric Correction) ในพื้นที่ศึกษาหาดเจ้าสำราญ จังหวัดเพชรบุรี หาดท้ายเหมือง จังหวัดพังงา และเกาะหมาก จังหวัดตราด

ผลเบื้องต้นนั้น Lyzenga Algorithm มีความเหมาะสมกับพื้นที่แรก กับ Stumpf Algorithm มีความเหมาะสมกับสองพื้นที่หลัง โดยการเลือกภาพแบบไม่ต้องตรวจแก้ให้ผลลัผธ์ที่ดีกว่า ดังนั้นควรเลือกภาพให้ดีตั้งแต่เริ่มต้น นำเข้าทำแบบจำลองได้เลย ความถูกต้องอยู่ในระดับ 1 ถึง 3 เมตร

การศึกษานี้ยังมีประเด็นที่สามารถศึกษาต่อได้มากมาย ทั้งเรื่องการลด bias ของการวิจัย การเลี่ยง manual selection การตรวจแก้ภาพและค่าระดับให้ดีขึ้นพร้อมต่อการทำแบบจำลอง รูปแบบอัลกอริทึมที่เข้ากับธรรมชาติได้ดีกว่าสองอัลกอริทึมที่นำมาวิจัย และอื่นๆ 
