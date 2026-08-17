# تعليمات خطوة بخطوة للمتعلم — إكمال واجب Emotion Detector (16/16)

> **النظام الرسمي للتقييم**: 16 نقطة (Task 1..8)، النجاح 75% = 12 نقطة.
> الحل في هذا المستودع يغطي **16/16 = 100%**.
> المستودع: https://github.com/basharalameed/emotion-detector

## القاعدة الذهبية (أهم خطأ يخسر نقاطاً)
- أسئلة **النص**: انسخ **محتوى الملف** كاملاً والصقه في خانة الإجابة.
- **ممنوع** لصق مسار الملف (مثل `Task_2_watson_app\2b_application_creation`) — المصحح يرفضه ويعتبر الإجابة ناقصة.
- أسئلة **الرابط (URL)**: انسخ الرابط والصقه في خانة "Enter website URL".
- أسئلة **الصورة**: استخدم زر **Upload** وارفع ملف الـ PNG من حاسوبك — لا تنسخ نصاً.
- لا تختصر أو تحذف أي جزء من الكود — المطلوب دائماً **المحتوى الكامل**.

---

## Task 1 — سؤال 1 (رابط) ⭐ نقطة واحدة
**المطلوب**: رابط عام لملف README.md الذي يحتوي اسم المشروع وتفاصيله.
**الإجابة**: الصق هذا الرابط في خانة Enter website URL:
```
https://github.com/basharalameed/emotion-detector/blob/main/README.md
```

## Task 2 — سؤالان 2 و 3 ⭐ نقطتان
**س2 (نص)**: كود `emotion_detection.py` الذي يعرض دالة التطبيق.
**الإجابة**: افتح الملف `Task_2_watson_app\2a_emotion_detection` → انسخ **كل** المحتوى → الصقه.

**س3 (نص)**: مخرجات طرفية تثبت أن التطبيق استُورد واختُبر دون أخطاء.
**الإجابة**: افتح `Task_2_watson_app\2b_application_creation` → انسخ المخرجات كاملة → الصقه.

## Task 3 — سؤالان 4 و 5 ⭐ نقطتان
**س4 (نص)**: كود الدالة المعدّلة `emotion_detector` بالصيغة الصحيحة (قاموس + dominant_emotion).
**الإجابة**: افتح `Task_3_output_format\3a_output_formatting` → انسخ كاملاً → الصقه.

**س5 (نص)**: مخرجات تثبت صحة صيغة التنسيق.
**الإجابة**: افتح `Task_3_output_format\3b_formatted_output_test` → انسخ كاملاً → الصقه.

## Task 4 — سؤالان 6 و 7 ⭐ نقطتان
**س6 (رابط)**: رابط عام لملف `__init__.py` الذي يستورد وحدة التطبيق.
**الإجابة**: الصق الرابط:
```
https://github.com/basharalameed/emotion-detector/blob/main/EmotionDetection/__init__.py
```

**س7 (نص)**: مخرجات تثبت أن `EmotionDetection` حزمة صالحة (جملة الاستيراد + درجات المشاعر).
**الإجابة**: افتح `Task_4_package\4b_packaging_test` → انسخ كاملاً → الصقه.

## Task 5 — سؤالان 8 و 9 ⭐ نقطتان
**س8 (نص)**: كود ملف `test_emotion_detection.py` باختبارات الوحدة المطلوبة.
**الإجابة**: افتح `Task_5_unit_tests\5a_unit_testing` → انسخ كاملاً → الصقه.

**س9 (نص)**: مخرجات نجاح اختبارات الوحدة (5 اختبارات ... ok).
**الإجابة**: افتح `Task_5_unit_tests\5b_unit_testing_result` → انسخ كاملاً → الصقه.

## Task 6 — سؤالان 10 و 11 ⭐ نقطتان
**س10 (نص)**: كود `server.py` الكامل للنشر عبر Flask.
**الإجابة**: افتح `Task_6_flask_deployment\6a_server` → انسخ كاملاً → الصقه.

**س11 (صورة)**: ارفع اللقطة المسمّاة `6b_deployment_test.png` التي تثبت تشغيل التطبيق.
**الإجابة**: زر **Upload** ← اختر من حاسوبك:
```
D:\امتحان\emotion-detector\Task_6_flask_deployment\6b_deployment_test.png
```

## Task 7 — ثلاثة أسئلة 12 و 13 و 14 ⭐ 3 نقاط
**س12 (نص)**: كود دالة `emotion_detector` المحدّثة لمعالجة رمز الحالة 400.
**الإجابة**: افتح `Task_7_error_handling\7a_error_handling_function` → انسخ كاملاً → الصقه.

**س13 (نص)**: كود `server.py` لمعالجة الإدخال الفارغ (`Invalid text! Please try again!`).
**الإجابة**: افتح `Task_7_error_handling\7b_error_handling_server` → انسخ كاملاً → الصقه.

**س14 (صورة)**: ارفع اللقطة `7c_error_handling_interface.png` التي تثبت عمل معالجة الأخطاء.
**الإجابة**: زر **Upload** ← اختر من حاسوبك:
```
D:\امتحان\emotion-detector\Task_7_error_handling\7c_error_handling_interface.png
```

## Task 8 — سؤالان 15 و 16 ⭐ نقطتان
**س15 (نص)**: كود `server.py` الذي يُظهر تنفيذ التحليل الساكن (دالة `run_static_code_analysis`).
**الإجابة**: افتح `Task_8_static_analysis\8a_server_modified` → انسخ كاملاً → الصقه.

**س16 (نص)**: مخرجات طرفية بالدرجة الكاملة للتحليل الساكن.
**الإجابة**: افتح `Task_8_static_analysis\8b_static_code_analysis` → انسخ كاملاً → الصقه.
(النتيجة المثبتة: **Your code has been rated at 10.00/10**)

---

## خطوات الإنهاء
1. أجب عن جميع الأسئلة الـ 16 بالطريقة أعلاه.
2. راجع: كل سؤال نصي حوى **محتوى** وليس مساراً، وكل صورة رُفعت بملفها الفعلي، وكل رابط سليم.
3. اضغط **Submit assignment**.
4. النتيجة المتوقعة: **16/16 = 100%** (النجاح من 12).

## إذا ظهرت ملاحظة "The submission does not include..."
- هذا يعني أنك لصقت **المسار** بدل المحتوى → افتح الملف المذكور في الجدول وانسخ محتواه الحقيقي كاملاً ثم أعد الإرسال.