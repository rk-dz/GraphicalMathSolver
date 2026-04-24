import re                                             # استدعاء مكتبة التعابير النمطية لمعالجة وتنسيق النصوص الرياضية
import math                                           # استدعاء مكتبة الرياضيات القياسية لإجراء العمليات الحسابية الأساسية
import customtkinter as ctk                           # استدعاء مكتبة واجهة المستخدم لتصميم النوافذ الرسومية الحديثة
import matplotlib as mpl                              # اسدعاء مكتبة الرسم البياني لضبط الخصائص البصرية العامة
import matplotlib.pyplot as plt                       # استدعاء واجهة الرسم البياني لإنشاء المحاور والأشكال الهندسية
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # استدعاء فئة دمج الرسم البياني ضمن واجهة البرنامج
import sympy as sp                                    # استدعاء مكتبة الرياضيات الرمزية لتحليل وحل المعادلات جبرياً
from tkinter import messagebox                        # استدعاء وحدة الرسائل لعرض التنبيهات والأخطاء للمستخدم بصرياً


# ══════════════════════════════════════════════════════════════════════════════
# القسم 1 — الألوان والإعدادات البصرية للمشروع
# ══════════════════════════════════════════════════════════════════════════════

ctk.set_appearance_mode("dark")                       # تعيين السمة المظلمة كإعداد افتراضي لواجهة المستخدم الرسومية

BG      = "#0d1117"                                   # تعريف لون الخلفية الأساسية مستوحى من واجهات التطبيقات الحديثة
PANEL   = "#161b22"                                   # تعريف لون اللوحات الجانبية ومساحة عرض الرسم البياني
CARD    = "#21262d"                                   # تعريف لون الحقول وبطاقات إدخال البيانات في الواجهة
CARD_H  = "#30363d"                                   # تعريف لون تفاعلي للبطاقات عند تمرير مؤشر الفأرة فوقها
EDGE    = "#30363d"                                   # تعريف لون الحدود والخطوط الفاصلة لتنظيم الواجهة
BLUE    = "#3b82f6"                                   # تعريف اللون الأزرق الرئيسي المخصص للإجراءات الأساسية
BLUE_H  = "#60a5fa"                                   # تعريف لون تفاعلي أفتح للأزرار الزرقاء عند التمرير
AMBER   = "#fbbf24"                                   # تعريف اللون الكهرماني لتمييز نقاط التقاطع والحلول
RED     = "#ef4444"                                   # تعريف اللون الأحمر المخصص للإجراءات الحرجة كالحذف
RED_H   = "#f87171"                                   # تعريف لون تفاعلي للأزرار الحمراء عند التمرير
TEXT    = "#f0f2f5"                                   # تعريف لون النصوص الأساسية لضمان تباين عالٍ للقراءة
MUTED   = "#8b949e"                                   # تعريف لون النصوص الثانوية والملاحظات الجانبية

CURVE_COLORS =[                                      # تهيئة قائمة بالألوان المخصصة لرسم المنحنيات المتعددة
    "#3b82f6",                                        # تخصيص اللون الأزرق للمنحنى الأول
    "#14b8a6",                                        # تخصيص اللون الفيروزي للمنحنى الثاني
    "#a78bfa",                                        # تخصيص اللون البنفسجي للمنحنى الثالث
    "#f97316",                                        # تخصيص اللون البرتقالي للمنحنى الرابع
    "#f43f5e",                                        # تخصيص اللون الوردي للمنحنى الخامس
    "#22c55e",                                        # تخصيص اللون الأخضر للمنحنى السادس
]                                                     # إنهاء تعريف قائمة ألوان المنحنيات

mpl.rcParams.update({                                 # تحديث قاموس إعدادات مكتبة الرسم البياني ليتوافق مع السمة المظلمة
    "figure.facecolor":   BG,                         # تعيين لون خلفية الشكل الخارجي للرسم البياني
    "axes.facecolor":     PANEL,                      # تعيين لون خلفية المحاور ومساحة الشبكة الداخلية
    "axes.edgecolor":     EDGE,                       # تعيين لون إطار مساحة الرسم البياني
    "axes.labelcolor":    TEXT,                       # تعيين لون نصوص تسميات المحاور الديكارتية
    "axes.labelsize":     11,                         # تحديد حجم الخط لتسميات المحاور
    "xtick.color":        MUTED,                      # تعيين لون علامات وتدريجات المحور السيني
    "ytick.color":        MUTED,                      # تعيين لون علامات وتدريجات المحور الصادي
    "text.color":         TEXT,                       # تعيين اللون العام للنصوص داخل مساحة الرسم
    "grid.color":         CARD_H,                     # تعيين لون خطوط الشبكة المساعدة لتتناغم مع الخلفية
    "grid.linestyle":     "--",                       # تحديد نمط خطوط الشبكة لتكون متقطعة
    "grid.linewidth":     0.7,                        # تحديد سماكة خطوط الشبكة لتكون هادئة وغير مزعجة
    "legend.facecolor":   CARD,                       # تعيين لون خلفية مفتاح الرسم البياني للمنحنيات
    "legend.edgecolor":   EDGE,                       # تعيين لون إطار مفتاح الرسم البياني
    "legend.labelcolor":  TEXT,                       # تعيين لون نصوص مفتاح الرسم البياني
    "axes.spines.top":    False,                      # إخفاء الحد العلوي لإطار الرسم لتحسين المظهر العصري
    "axes.spines.right":  False,                      # إخفاء الحد الأيمن لإطار الرسم لتقليل التشتت البصري
})                                                    # إنهاء تحديث إعدادات مكتبة الرسم البياني


# ══════════════════════════════════════════════════════════════════════════════
# القسم 2 — دوال البنية التحتية لتوليد عناصر واجهة المستخدم
# ══════════════════════════════════════════════════════════════════════════════

def make_sidebar(parent, width: int = 260) -> ctk.CTkFrame: # تعريف دالة لتوليد اللوحة الجانبية الحاوية لأدوات التحكم
    f = ctk.CTkFrame(parent, width=width, fg_color=PANEL, corner_radius=16) # إنشاء إطار اللوحة مع تحديد العرض ولون الخلفية
    f.pack(side="left", fill="y", padx=(0, 10), pady=4) # تموضع اللوحة في الجهة اليسرى مع التمدد العمودي وضبط الهوامش
    f.pack_propagate(False)                           # تعطيل خاصية الانكماش التلقائي للإطار ليحافظ على عرضه الثابت
    return f                                          # إرجاع كائن اللوحة الجانبية للاستخدام لاحقاً

def make_section_label(parent, text: str):            # تعريف دالة لتوليد عناوين الأقسام الفرعية داخل اللوحات
    ctk.CTkLabel(parent, text=text.upper(), font=ctk.CTkFont(size=10, weight="bold"), text_color=MUTED).pack(anchor="w", padx=10, pady=(8, 2)) # إنشاء وتنسيق العنوان ثم إدراجه بمحاذاة اليسار

def make_divider(parent):                             # تعريف دالة لتوليد خطوط فصل بصرية بين مكونات الواجهة
    ctk.CTkFrame(parent, height=1, fg_color=EDGE).pack(fill="x", padx=10, pady=4) # إنشاء إطار بارتفاع بكسل واحد وتمديده أفقياً ليعمل كفاصل

def make_card(parent) -> ctk.CTkFrame:                # تعريف دالة لتوليد بطاقات تجميع واحتواء الحقول النصية
    return ctk.CTkFrame(parent, fg_color=CARD, corner_radius=12, border_width=1, border_color=EDGE) # إرجاع إطار بخلفية مخصصة وحواف دائرية وحدود رقيقة

def make_entry(parent, placeholder: str = "", width: int = 170) -> ctk.CTkEntry: # تعريف دالة لتوليد حقول إدخال البيانات القياسية
    return ctk.CTkEntry(parent, placeholder_text=placeholder, width=width, fg_color=BG, border_color=EDGE, text_color=TEXT, font=ctk.CTkFont(family="Courier", size=13), height=30, corner_radius=10) # إرجاع حقل إدخال مهيأ بخط أحادي العرض لدعم المعادلات

def make_textbox(parent, height: int = 160) -> ctk.CTkTextbox: # تعريف دالة لتوليد مساحة عرض النصوص (للقراءة فقط)
    tb = ctk.CTkTextbox(parent, height=height, fg_color=CARD, font=ctk.CTkFont(family="Courier", size=12), text_color=TEXT, border_color=EDGE, border_width=1, corner_radius=12) # إنشاء كائن مربع النص مع تنسيق الألوان والخطوط
    tb.pack(fill="both", expand=True, padx=10, pady=(2, 8)) # إدراج مربع النص مع السماح له بالتمدد لملء المساحة المتاحة
    tb.configure(state="disabled")                    # تعطيل إمكانية التحرير اليدوي لمربع النص من قبل المستخدم
    return tb                                         # إرجاع كائن مربع النص

def update_textbox(tb: ctk.CTkTextbox, content: str): # تعريف دالة لتحديث محتوى مربعات النص برمجياً
    tb.configure(state="normal")                      # تفعيل حالة التحرير مؤقتاً للسماح بتعديل المحتوى
    tb.delete("1.0", "end")                           # مسح كافة البيانات السابقة الموجودة في المربع
    if content:                                       # التحقق من وجود محتوى جديد لإضافته
        tb.insert("end", content)                     # إدراج المحتوى الجديد في نهاية مربع النص
    tb.configure(state="disabled")                    # إعادة تعطيل حالة التحرير لحماية المحتوى

def _make_btn(parent, text: str, command, fg: str, hover: str, border: bool = False, icon: str = "") -> ctk.CTkButton: # دالة أساسية محمية لتوليد أزرار تفاعلية موحدة النمط
    label = f"{icon}   {text}" if icon else text      # تجهيز التسمية بدمج الأيقونة مع النص في حال توفرها
    return ctk.CTkButton(parent, text=label, command=command, fg_color=fg, hover_color=hover, border_width=1 if border else 0, border_color=EDGE, font=ctk.CTkFont(size=14, weight="bold"), height=34, corner_radius=12) # إرجاع زر مهيأ بالخصائص المرئية ووظيفة الاستدعاء

def primary_btn(p, t, c, i=""): return _make_btn(p, t, c, BLUE, BLUE_H, icon=i)   # دالة مغلفة لتوليد أزرار الإجراءات الأساسية باللون الأزرق
def secondary_btn(p, t, c, i=""): return _make_btn(p, t, c, CARD, CARD_H, border=True, icon=i) # دالة مغلفة لتوليد أزرار الإجراءات الثانوية بلون رمادي
def danger_btn(p, t, c, i=""): return _make_btn(p, t, c, RED, RED_H, icon=i)      # دالة مغلفة لتوليد أزرار الإجراءات الحرجة باللون الأحمر

def build_range_card(parent, label: str, default_min: str, default_max: str): # تعريف دالة لبناء بطاقة مخصصة لتحديد النطاقات الرقمية
    make_section_label(parent, label)                 # إنشاء عنوان القسم التعريفي للبطاقة
    r = make_card(parent)                             # توليد بطاقة الاحتواء الأساسية
    r.pack(fill="x", padx=10, pady=8)                 # إدراج البطاقة مع السماح لها بالتمدد الأفقي

    entry_min = make_entry(r, width=80)               # إنشاء حقل إدخال للحد الأدنى للنطاق
    entry_max = make_entry(r, width=80)               # إنشاء حقل إدخال للحد الأقصى للنطاق
    entry_min.insert(0, default_min)                  # حقن القيمة الافتراضية للحد الأدنى
    entry_max.insert(0, default_max)                  # حقن القيمة الافتراضية للحد الأقصى

    for col, (txt, widget) in enumerate([("from", entry_min), ("to", entry_max)]): # تكرار العملية لترتيب الحقول وعناوينها أفقياً
        ctk.CTkLabel(r, text=txt, text_color=MUTED, font=ctk.CTkFont(size=11, weight="bold")).grid(row=0, column=col * 2, padx=(8 if col == 0 else 4, 2), pady=4) # وضع عنوان الحقل في الشبكة
        widget.grid(row=0, column=col * 2 + 1, padx=(2, 6 if col == 1 else 2), pady=4) # وضع حقل الإدخال المقابل في الشبكة

    return entry_min, entry_max                       # إرجاع مراجع الحقول لاستخلاص البيانات منها لاحقاً

def read_range(entry_min, entry_max) -> tuple:        # تعريف دالة لاستخلاص والتحقق من صحة بيانات النطاقات الرقمية
    vmin = float(entry_min.get())                     # تحويل القيمة النصية للحد الأدنى إلى عدد عشري
    vmax = float(entry_max.get())                     # تحويل القيمة النصية للحد الأقصى إلى عدد عشري
    if vmin >= vmax:                                  # التحقق من المنطق الرياضي (الحد الأدنى يجب أن يكون أصغر بدقة)
        raise ValueError("Minimum must be strictly less than maximum.") # إثارة استثناء برمجي في حال عدم تطابق المنطق
    return vmin, vmax                                 # إرجاع القيم الرقمية المعتمدة


# ══════════════════════════════════════════════════════════════════════════════
# القسم 3 — دوال مساعدة رياضية لتعويض وظائف مكتبة Numpy
# ══════════════════════════════════════════════════════════════════════════════

def generate_linspace(start: float, stop: float, num: int) -> list: # تعريف دالة لتوليد فضاء خطي من الأرقام بالتساوي
    if num <= 1: return [float(start)]                # معالجة حالة الطلب لنقطة واحدة فقط أو أقل لتجنب الأخطاء
    step = (stop - start) / (num - 1)                 # حساب الخطوة الثابتة بين كل نقطة والتي تليها
    return[start + i * step for i in range(num)]     # بناء وإرجاع قائمة النقاط باستخدام الاستيعاب

def calculate_percentile(data: list, p: float) -> float: # تعريف دالة لحساب المئينيات الإحصائية للبيانات
    if not data: return 0.0                           # معالجة حالة القائمة الفارغة لتجنب أخطاء الفهرسة
    sorted_data = sorted(data)                        # فرز البيانات تصاعدياً كشرط أساسي لحساب المئين
    k = (len(sorted_data) - 1) * (p / 100.0)          # حساب الفهرس النسبي ذو الفاصلة العائمة
    f = math.floor(k)                                 # استخراج الجزء الصحيح الأدنى من الفهرس
    c = math.ceil(k)                                  # استخراج الجزء الصحيح الأعلى من الفهرس
    if f == c: return sorted_data[int(k)]             # إرجاع القيمة المباشرة إذا كان الفهرس عدداً صحيحاً تماماً
    return sorted_data[int(f)] * (c - k) + sorted_data[int(c)] * (k - f) # إجراء استيفاء خطي للحصول على دقة أعلى


# ══════════════════════════════════════════════════════════════════════════════
# القسم 4 — بناء نافذة المعلومات التعريفية للمشروع
# ══════════════════════════════════════════════════════════════════════════════

class AboutWindow(ctk.CTkToplevel):
    INFO =[
        ("Project",       "Graphical Math Solver"),
        ("Level",         "4th Year Middle School"),
        ("School",        "Alwan Brothers Middle School\n"
                          "                Mohamed & Mahmoud"),
        ("Project Owner", "Abed Rafik"),
    ]

    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.geometry("440x295")
        self.resizable(False, False)
        self.configure(fg_color=BG)
        self.after(150, self._activate)  
        self._build()

    def _activate(self):
        try:
            self.grab_set()
            self.focus_force()
        except Exception:
            pass

    def _build(self):
        # الشريط العلوي 
        hdr = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=0, height=60)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        ctk.CTkFrame(hdr, width=4, fg_color=BLUE, corner_radius=0).pack(   # شريط أزرق جانبي
            side="left", fill="y")
        ctk.CTkLabel(hdr, text="  About this Project",
                     font=ctk.CTkFont(size=17, weight="bold"),
                     text_color=TEXT).pack(side="left", padx=14, pady=18)

        # جسم النافذة
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=30, pady=18)

        for field, value in self.INFO:
            row = ctk.CTkFrame(body, fg_color="transparent")
            row.pack(fill="x", pady=5)
            ctk.CTkLabel(row, text=field,
                         font=ctk.CTkFont(size=12, weight="bold"),
                         text_color=MUTED, width=110, anchor="w").pack(side="left")
            ctk.CTkLabel(row, text="│", text_color=EDGE).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=value,
                         font=ctk.CTkFont(size=13), text_color=TEXT,
                         anchor="w", justify="left").pack(side="left")

        ctk.CTkFrame(body, height=1, fg_color=EDGE).pack(fill="x", pady=(14, 10))
        ctk.CTkLabel(body,
                     text="Built with Python  ·  customtkinter  ·  matplotlib  ·  sympy  ·  math",
                     font=ctk.CTkFont(size=10), text_color=MUTED).pack()


# هيكل وإدارة لوحة الرسم البياني الأساسية ══════════════════════════════════════════════════════════════════════════════


class PlotCanvas(ctk.CTkFrame):                       # تعريف فئة لتغليف وإدارة كائن الرسم البياني ضمن واجهة المستخدم
    AXIS_COLOR  = "#a1aab5"                           # تخصيص لون فاتح وبارز لمحاور الصفر الأساسية لتمييزها عن الشبكة
    AXIS_WIDTH  = 2.0                                 # تحديد سماكة بارزة لخطوط محاور الإحداثيات لتعزيز وضوحها
    CURVE_WIDTH = 2.5                                 # تحديد السماكة القياسية للمنحنيات الرسومية
    POINT_SIZE  = 90                                  # تحديد الحجم القياسي للنقاط المبعثرة المرسومة

    def __init__(self, parent):                       # تعريف دالة التهيئة للفئة لإنشاء لوحة الرسم
        super().__init__(parent, fg_color=BG, corner_radius=16) # استدعاء دالة التهيئة للفئة الأساسية مع تطبيق النمط المرئي
        self.fig, self.ax = plt.subplots(figsize=(6.0, 6.0), dpi=100) # تهيئة كائن الشكل والمحاور من مكتبة الرسم بأبعاد مربعة
        self.fig.patch.set_facecolor(BG)              # تطبيق لون الخلفية العام على الشكل لاخفاء الحواف البيضاء
        self._mpl = FigureCanvasTkAgg(self.fig, master=self) # دمج كائن الرسم البياني داخل بنية واجهة المستخدم الرسومية
        self._mpl.get_tk_widget().pack(fill="both", expand=True, padx=8, pady=8) # إدراج كائن الدمج وتمديده ليغطي الإطار المخصص
        self.reset()                                  # استدعاء دالة إعادة الضبط لتهيئة المحاور لأول مرة

    def reset(self, xlim: tuple = (-10, 10), ylim: tuple = (-10, 10)): # تعريف دالة لإعادة تهيئة ورسم الشبكة والمحاور
        self.ax.clear()                               # مسح كافة الكائنات الرسومية السابقة من المحاور
        self.ax.set_facecolor(PANEL)                  # إعادة تطبيق لون الخلفية المخصص لمساحة الشبكة
        self.ax.grid(True, alpha=0.6)                 # تفعيل رسم شبكة الإحداثيات الخلفية مع إضافة شفافية طفيفة
        
        self.ax.set_aspect('equal', adjustable='box') # فرض نسبة أبعاد متساوية لضمان تربيع شبكة الإحداثيات هندسياً

        self.ax.axhline(0, color=self.AXIS_COLOR, lw=self.AXIS_WIDTH, zorder=3) # رسم خط المحور السيني عند الصفر وجعله فوق الشبكة
        self.ax.axvline(0, color=self.AXIS_COLOR, lw=self.AXIS_WIDTH, zorder=3) # رسم خط المحور الصادي عند الصفر وجعله فوق الشبكة

        arrow_props = dict(arrowstyle="->", color=self.AXIS_COLOR, lw=self.AXIS_WIDTH, mutation_scale=14) # تعريف خصائص أسهم الاتجاهات للمحاور
        
        self._arr_x = self.ax.annotate("", xy=(1, 0), xytext=(0, 0), xycoords=self.ax.get_yaxis_transform(), textcoords=self.ax.get_yaxis_transform(), arrowprops=arrow_props, annotation_clip=False, zorder=4) # إضافة سهم نهاية المحور السيني بمحاذاة حافة الإطار
        self._arr_y = self.ax.annotate("", xy=(0, 1), xytext=(0, 0), xycoords=self.ax.get_xaxis_transform(), textcoords=self.ax.get_xaxis_transform(), arrowprops=arrow_props, annotation_clip=False, zorder=4) # إضافة سهم نهاية المحور الصادي بمحاذاة حافة الإطار

        self.ax.set_xlabel("Abscissas Axis  →  x", fontsize=11, labelpad=10) # تعيين تسمية المحور السيني مع ضبط التباعد
        self.ax.set_ylabel("Ordinates Axis  →  y", fontsize=11, labelpad=10, rotation=90) # تعيين تسمية المحور الصادي مع تدوير النص

        self.ax.set_xlim(xlim)                        # تطبيق حدود العرض المحددة للمحور السيني
        self.ax.set_ylim(ylim)                        # تطبيق حدود العرض المحددة للمحور الصادي

        x_span = xlim[1] - xlim[0]                    # حساب المدى الإجمالي للمحور السيني
        y_span = ylim[1] - ylim[0]                    # حساب المدى الإجمالي للمحور الصادي
        x_step = 1 if x_span <= 30 else int(math.ceil(x_span / 20)) # تحديد خطوة تدريج المحور السيني ديناميكياً لحماية الأداء
        y_step = 1 if y_span <= 30 else int(math.ceil(y_span / 20)) # تحديد خطوة تدريج المحور الصادي ديناميكياً لحماية الأداء

        min_x, max_x = int(math.floor(xlim[0])), int(math.ceil(xlim[1])) + 1 # حساب النطاق الصحيح لتوليد علامات المحور السيني
        min_y, max_y = int(math.floor(ylim[0])), int(math.ceil(ylim[1])) + 1 # حساب النطاق الصحيح لتوليد علامات المحور الصادي
        self.ax.set_xticks(list(range(min_x, max_x, x_step))) # تطبيق التدريجات المحسوبة على المحور السيني
        self.ax.set_yticks(list(range(min_y, max_y, y_step))) # تطبيق التدريجات المحسوبة على المحور الصادي
        
        self.ax.tick_params(labelsize=10)             # توحيد حجم خطوط تسميات التدريجات للمحاور
        self.refresh()                                # استدعاء دالة التحديث لتطبيق التغييرات بصرياً

    def refresh(self):                                # تعريف دالة لإعادة رسم الواجهة بعد أي تعديل
        self.fig.tight_layout(pad=1.8)                # تحسين تخطيط العناصر داخل الشكل لتجنب التداخل
        self._mpl.draw()                              # توجيه أمر مباشر للمكتبة لإعادة عرض المشهد المحدث


# المعالجة وتحليل المعادلات  ══════════════════════════════════════════════════════════════════════════════


def parse_equation(raw: str) -> sp.Eq:                # تعريف دالة لتحليل النصوص الرياضية وتحويلها لمعادلات رمزية
    s = raw.strip().replace(" ", "")                  # إزالة المسافات البيضاء من السلسلة النصية لتسهيل التحليل
    if "=" not in s: raise ValueError(f"Missing '=' in: {raw!r}") # إثارة خطأ برمجي في حال غياب مشغل المساواة الأساسي
    s = s.replace("^", "**")                          # استبدال رمز القوة الشائع بالرمز المعتمد في بايثون
    
    for _ in range(2):                                # تنفيذ دورة مزدوجة لمعالجة حالات التجاور الضمني للعمليات
        s = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", s)    # إدراج مشغل الضرب بين الأرقام والمتغيرات المجاورة
        s = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", s)    # إدراج مشغل الضرب بين المتغيرات والأرقام المجاورة
        
    lhs, rhs = s.split("=", 1)                        # تقسيم السلسلة النصية إلى طرف أيمن وأيسر حول مشغل المساواة
    return sp.Eq(sp.sympify(lhs), sp.sympify(rhs))    # تحويل الأطراف إلى كائنات رمزية وبناء معادلة جبرية

def lambdify_safe(sym_expr, x_sym, x_vals: list) -> list: # تعريف دالة لتوليد قيم دالة رياضية بشكل آمن برمجياً
    f = sp.lambdify(x_sym, sym_expr, "math")          # تحويل التعبير الرمزي إلى دالة بايثون قابلة للتنفيذ باستخدام مكتبة الرياضيات
    result =[]                                       # تهيئة قائمة فارغة لتخزين النتائج العددية
    
    for x in x_vals:                                  # بدء حلقة التكرار على جميع نقاط الفضاء الخطي
        try:                                          # بدء كتلة معالجة الاستثناءات للعمليات الحسابية
            y = float(f(x))                           # تقييم الدالة عند النقطة الحالية وتحويل الناتج لقيمة عشرية
            if math.isnan(y) or abs(y) > 1e4:         # فحص ما إذا كان الناتج غير معرف أو يمثل قيمة انفجارية شاذة
                result.append(float('nan'))           # إدراج قيمة غير معرفة لتجاهل رسم النقطة الشاذة
            else:                                     # في حال كانت القيمة صالحة رياضياً وضمن النطاق المقبول
                result.append(y)                      # إدراج القيمة المحسوبة في قائمة النتائج
        except Exception:                             # التقاط أي استثناء رياضي (مثل القسمة على صفر أو اللوغاريتم السالب)
            result.append(float('nan'))               # معالجة الخطأ بإدراج قيمة غير معرفة بصمت
            
    if len(result) > 1:                               # التحقق من وجود نقاط كافية لإجراء تحليل التجاور للمقاربات
        for i in range(1, len(result)):               # بدء حلقة تكرار لفحص الفروق بين النقاط المتجاورة
            y1, y2 = result[i-1], result[i]           # استخراج القيمتين المتجاورتين للتحليل
            if not math.isnan(y1) and not math.isnan(y2): # التأكد من صلاحية كلتا القيمتين لإجراء الطرح
                if abs(y2 - y1) > 50:                 # فحص وجود قفزة عملاقة تشير إلى خط مقارب عمودي وهمي
                    result[i] = float('nan')          # فصل المنحنى برمجياً عن طريق تحويل النقطة لقيمة غير معرفة
                    
    return result                                     # إرجاع قائمة النتائج النهائية والجاهزة للرسم



#  تبويب تعيين ورسم النقاط المستقلة ══════════════════════════════════════════════════════════════════════════════

class PointsTab(ctk.CTkFrame):                        # تعريف فئة لتبويب مخصص لإدارة ورسم الإحداثيات الديكارتية
    def __init__(self, parent):                       # تعريف دالة التهيئة للفئة الحالية
        super().__init__(parent, fg_color="transparent") # استدعاء دالة التهيئة الأساسية مع جعل الخلفية شفافة
        self.points: list[tuple[float, float, str]] =[] # تهيئة قائمة فارغة لتخزين سجلات النقاط المدخلة
        self._build_ui()                              # استدعاء دالة بناء مكونات واجهة المستخدم للتبويب

    def _build_ui(self):                              # تعريف دالة مخصصة لترتيب عناصر التبويب بصرياً
        left = make_sidebar(self)                     # توليد واستدعاء اللوحة الجانبية لأدوات التحكم
        self._build_header(left)                      # بناء وإدراج ترويسة التبويب في اللوحة الجانبية
        self._build_input_card(left)                  # بناء وإدراج بطاقة إدخال إحداثيات النقاط
        self._build_list_section(left)                # بناء وإدراج قسم عرض قائمة النقاط المسجلة
        self._build_action_buttons(left)              # بناء وإدراج أزرار العمليات التنفيذية

        self.canvas = PlotCanvas(self)                # إنشاء مثيل للوحة الرسم البياني المخصصة
        self.canvas.pack(side="right", fill="both", expand=True, pady=4) # إدراج لوحة الرسم في الجهة اليمنى وتمديدها بالكامل

    def _build_header(self, p):                       # تعريف دالة لتهيئة الترويسة الوصفية للتبويب
        ctk.CTkLabel(p, text="Points on Plane", font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT).pack(anchor="w", padx=10, pady=(10, 2)) # إدراج العنوان الرئيسي للتبويب
        ctk.CTkLabel(p, text="Plot points using Cartesian coordinates.", font=ctk.CTkFont(size=11), text_color=MUTED).pack(anchor="w", padx=10, pady=(0, 4)) # إدراج نص وصفي فرعي لوظيفة التبويب
        make_divider(p)                               # إدراج خط فاصل تنظيمي أسفل الترويسة

    def _build_input_card(self, p):                   # تعريف دالة لبناء بطاقة إدخال بيانات النقطة
        make_section_label(p, "New Point")            # إدراج عنوان قسم الإدخال
        c = make_card(p)                              # إنشاء بطاقة الاحتواء لحقول الإدخال
        c.pack(fill="x", padx=10, pady=8)             # إدراج البطاقة مع السماح لها بالتمدد الأفقي
        c.columnconfigure(1, weight=1)                # ضبط إعدادات الشبكة للسماح للعمود الثاني بالتمدد

        self.entry_x     = make_entry(c, placeholder="0",   width=180) # إنشاء حقل إدخال إحداثيات المحور السيني
        self.entry_y     = make_entry(c, placeholder="0",   width=180) # إنشاء حقل إدخال إحداثيات المحور الصادي
        self.entry_label = make_entry(c, placeholder="A",   width=180) # إنشاء حقل إدخال التسمية الوصفية للنقطة

        for i, (name, widget) in enumerate([("x          ", self.entry_x), ("y          ", self.entry_y), ("Label   ", self.entry_label)]): # تكرار مصفوفة الحقول لتوزيعها في الشبكة
            ctk.CTkLabel(c, text=name, text_color=MUTED, font=ctk.CTkFont(size=12, weight="bold"), width=50, anchor="e").grid(row=i, column=0, padx=(4, 2), pady=2, sticky="e") # إدراج عنوان الحقل بمحاذاة اليمين
            widget.grid(row=i, column=1, padx=(2, 6), pady=2, sticky="ew") # إدراج حقل الإدخال المقابل والسماح له بالتمدد العرضي

    def _build_list_section(self, p):                 # تعريف دالة لبناء قسم عرض قائمة البيانات المدخلة
        make_divider(p)                               # إدراج خط فاصل تنظيمي
        make_section_label(p, "Points List")          # إدراج عنوان قسم عرض القائمة
        self.textbox = make_textbox(p)                # إنشاء واستدعاء مربع النص المخصص لعرض السجلات

    def _build_action_buttons(self, p):               # تعريف دالة لبناء وتوزيع أزرار التحكم السفلية
        make_divider(p)                               # إدراج خط فاصل تنظيمي
        danger_btn(p, "Clear All", self._on_clear, "⊗").pack(fill="x", padx=10, pady=(8, 20), side="bottom") # إدراج زر المسح الشامل في الأسفل مع زيادة الهامش السفلي
        secondary_btn(p, "Add Point", self._on_add, "⊕").pack(fill="x", padx=10, pady=(4, 8), side="bottom") # إدراج زر إضافة النقطة فوق زر المسح مباشرة

    def _on_add(self):                                # تعريف إجراء الاستجابة لحدث النقر على زر الإضافة
        try:                                          # التحقق من صحة المدخلات الرقمية
            x = float(self.entry_x.get())             # محاولة استخراج وتحويل قيمة السينات إلى عدد عشري
            y = float(self.entry_y.get())             # محاولة استخراج وتحويل قيمة الصادات إلى عدد عشري
        except ValueError:                            # التقاط استثناء فشل التحويل البرمجي
            messagebox.showerror("Input Error", "x and y must be numeric values.") # عرض رسالة خطأ للمستخدم توضح المشكلة
            return                                    # إيقاف تنفيذ الإجراء للانتظار لتصحيح المدخلات

        name = self.entry_label.get().strip() or f"P{len(self.points) + 1}" # استخراج التسمية أو توليد تسمية افتراضية في حال الفراغ
        self.points.append((x, y, name))              # تسجيل النقطة الجديدة في القائمة الداخلية للبيانات
        
        content = "".join(f"  {lbl:<6}  ({px:>8.3f}, {py:>8.3f})\n" for px, py, lbl in self.points) # بناء سلسلة نصية منسقة لجميع النقاط المسجلة
        update_textbox(self.textbox, content)         # تحديث مساحة العرض النصية بالسلسلة المنسقة
        for field in (self.entry_x, self.entry_y, self.entry_label): field.delete(0, "end") # مسح محتويات حقول الإدخال لتجهيزها للعملية التالية

        self._render()                                # استدعاء دالة الرسم لتحديث اللوحة البصرية بالنقاط الجديدة

    def _render(self):                                # تعريف دالة لإجراء الحسابات البصرية ورسم النقاط
        if not self.points: return                    # إيقاف التنفيذ في حال خلو قائمة النقاط من البيانات
        xs =[p[0] for p in self.points]              # استخلاص قائمة مستقلة لقيم السينات
        ys =[p[1] for p in self.points]              # استخلاص قائمة مستقلة لقيم الصادات

        margin = max(2.5, (max(xs) - min(xs)) * 0.25 + 2, (max(ys) - min(ys)) * 0.25 + 2) # حساب مسافة أمان ديناميكية لضمان عدم ملامسة النقاط للإطار
        self.canvas.reset(xlim=(min(xs) - margin, max(xs) + margin), ylim=(min(ys) - margin, max(ys) + margin)) # إعادة تهيئة اللوحة وتطبيق الحدود المحسوبة الجديدة

        for i, (x, y, name) in enumerate(self.points): # بدء حلقة تكرار لرسم النقاط فرادى وتخصيص ألوانها
            color = CURVE_COLORS[i % len(CURVE_COLORS)] # تعيين لون مميز من القائمة باستخدام معامل الباقي
            self.canvas.ax.scatter([x], [y], color=color, s=PlotCanvas.POINT_SIZE, zorder=5, edgecolors="white", linewidths=0.8) # رسم النقطة كدائرة مبعثرة وتحديد خصائصها
            self.canvas.ax.annotate(f"  {name}({x}, {y})", (x, y), fontsize=10, color=color, fontweight="bold") # إدراج تسمية النقطة وإحداثياتها كشرح توضيحي مجاور

        self.canvas.refresh()                         # استدعاء دالة التحديث لتطبيق التغييرات على المشهد البصري

    def _on_clear(self):                              # تعريف إجراء الاستجابة لحدث النقر على زر المسح
        self.points.clear()                           # مسح كافة البيانات من قائمة النقاط الداخلية
        update_textbox(self.textbox, "")              # إفراغ محتوى مساحة عرض النصوص بالكامل
        self.canvas.reset()                           # إعادة تهيئة اللوحة البصرية إلى حالتها الافتراضية



# تبويب إدخال ورسم الدوال الرياضية ══════════════════════════════════════════════════════════════════════════════


class FunctionsTab(ctk.CTkFrame):                     # تعريف فئة لتبويب مخصص لتحليل ورسم الدوال الرياضية المتصلة
    def __init__(self, parent):                       # تعريف دالة التهيئة للتبويب الحالي
        super().__init__(parent, fg_color="transparent") # استدعاء دالة التهيئة الأساسية مع إخفاء لون الخلفية
        self.functions: list[tuple[str, str]] =[]    # تهيئة قائمة فارغة لتخزين التعابير الرياضية المسجلة
        self._build_ui()                              # استدعاء دالة بناء الهيكل البصري للتبويب

    def _build_ui(self):                              # تعريف دالة متخصصة في ترتيب عناصر الواجهة
        left = make_sidebar(self)                     # توليد اللوحة الجانبية المخصصة لأدوات التحكم
        self._build_header(left)                      # بناء الترويسة التعريفية للتبويب
        self._build_function_card(left)               # بناء بطاقة إدخال التعابير الرياضية
        self._build_list_section(left)                # بناء قسم عرض الدوال المسجلة مسبقاً
        self._build_action_buttons(left)              # بناء أزرار التحكم بالعمليات

        self.canvas = PlotCanvas(self)                # إنشاء كائن لوحة الرسم البياني المخصصة للتبويب
        self.canvas.pack(side="right", fill="both", expand=True, pady=4) # إدراج لوحة الرسم في الواجهة ومنحها مساحة التمدد الكاملة

    def _build_header(self, p):                       # تعريف دالة بناء ترويسة التبويب
        ctk.CTkLabel(p, text="Function Plotter", font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT).pack(anchor="w", padx=10, pady=(10, 2)) # إدراج العنوان الرئيسي للتبويب الخاص بالدوال
        ctk.CTkLabel(p, text="Syntax:  *  multiply   **  power   /  divide   ^  power", font=ctk.CTkFont(size=11), text_color=MUTED).pack(anchor="w", padx=10, pady=(0, 4)) # إدراج تعليمات صياغة المعادلة للمستخدم
        make_divider(p)                               # إدراج خط فصل مرئي أسفل التعليمات

    def _build_function_card(self, p):                # تعريف دالة بناء بطاقة إدخال الدالة
        make_section_label(p, "New Function")         # إدراج تسمية لقسم الإدخال
        c = make_card(p)                              # توليد كائن البطاقة الحاوية
        c.pack(fill="x", padx=10, pady=8)             # إدراج البطاقة مع التمدد الأفقي لملء اللوحة الجانبية
        c.columnconfigure(1, weight=1)                # تفعيل التمدد التلقائي لحقول الإدخال في الشبكة

        self.entry_expr  = make_entry(c, placeholder="2*x + 1", width=180) # إنشاء حقل إدخال التعبير الرياضي للدالة
        self.entry_fname = make_entry(c, placeholder="f",        width=180) # إنشاء حقل إدخال التسمية الرمزية للدالة

        for i, (name, widget) in enumerate([("f(x)=", self.entry_expr), ("Label", self.entry_fname)]): # تكرار العملية لتموضع الحقول بصرياً
            ctk.CTkLabel(c, text=name, text_color=MUTED, font=ctk.CTkFont(size=12, weight="bold"), width=56, anchor="e").grid(row=i, column=0, padx=(4, 2), pady=2, sticky="e") # إدراج تسمية الحقل
            widget.grid(row=i, column=1, padx=(2, 6), pady=2, sticky="ew") # إدراج الحقل في الخلية المقابلة

    def _build_list_section(self, p):                 # تعريف دالة بناء قسم عرض الدوال المسجلة
        make_divider(p)                               # إدراج خط فاصل تنظيمي
        make_section_label(p, "Functions List")       # إدراج تسمية توضيحية لقسم القائمة
        self.textbox = make_textbox(p)                # إنشاء واستدعاء مساحة عرض النصوص

    def _build_action_buttons(self, p):               # تعريف دالة هيكلة الأزرار الوظيفية
        make_divider(p)                               # إدراج خط فاصل تنظيمي نهائي
        danger_btn(p, "Clear All", self._on_clear, "⊗").pack(fill="x", padx=10, pady=(8, 20), side="bottom") # إدراج زر مسح كافة الدوال مع هامش سفلي موسع
        secondary_btn(p, "Add Function", self._on_add, "⊕").pack(fill="x", padx=10, pady=(4, 8), side="bottom") # إدراج زر التأكيد والإضافة فوق زر المسح

    def _on_add(self):                                # تعريف إجراء الاستجابة لإضافة دالة جديدة
        expr = self.entry_expr.get().strip()          # استخراج التعبير الرياضي وتنظيفه من المسافات الزائدة
        if not expr: return                           # إيقاف التنفيذ في حال كان حقل التعبير فارغاً
        try:                                          # بدء كتلة التحقق الجبري من صحة التعبير
            sp.sympify(expr.replace("^", "**"))       # محاولة تحويل التعبير إلى كائن رمزي للتأكد من خلوه من الأخطاء النحوية
        except Exception:                             # التقاط أي خطأ نحوي في صياغة الرياضيات
            messagebox.showerror("Syntax Error", f"Cannot parse: {expr}\nExample: 2*x + 1   or   x**2 - 3") # عرض رسالة خطأ إرشادية للمستخدم
            return                                    # إيقاف التنفيذ لانتظار التصحيح

        name = self.entry_fname.get().strip() or f"f{len(self.functions) + 1}" # استخراج اسم الدالة أو توليد تسلسل تلقائي
        self.functions.append((expr, name))           # تسجيل الدالة الجديدة في القائمة المخصصة
        
        lines = "".join(f"  {n:<6}  f(x) = {e}\n" for e, n in self.functions) # تجميع وتنسيق نصوص الدوال لعرضها
        update_textbox(self.textbox, lines)           # تحديث مساحة العرض النصية بالدوال المجمعة
        self.entry_expr.delete(0, "end")              # مسح حقل إدخال التعبير الرياضي
        self.entry_fname.delete(0, "end")             # مسح حقل إدخال اسم الدالة
        self._render()                                # استدعاء دالة الرسم لمعالجة المنحنيات

    def _render(self):                                # تعريف دالة المعالجة البصرية لرسم المنحنيات
        if not self.functions: return                 # إيقاف التنفيذ العبثي في حال عدم وجود دوال
        x_sym = sp.Symbol("x")                        # تعريف المتغير الرمزي المستقل للتحليل الجبري
        
        probe_x = generate_linspace(-30, 30, 1500)    # توليد فضاء خطي اختباري موسع ضمن النطاق المطلوب[-30, 30] لفحص سلوك الدوال
        all_y_valid =[]                              # تهيئة قائمة لتجميع كافة المخرجات الصالحة إحصائياً
        for expr, _ in self.functions:                # التكرار على كافة التعابير المسجلة
            try:                                      # محاولة إجراء المعالجة الرياضية الآمنة
                sym = sp.sympify(expr.replace("^", "**")) # تحويل التعبير النصي لكائن رياضي رمزي
                y_vals = lambdify_safe(sym, x_sym, probe_x) # حساب قيم الدالة بشكل آمن متجنباً الانهيارات
                valid = [y for y in y_vals if math.isfinite(y)] # تصفية واستخلاص القيم الرقمية المحدودة فقط
                all_y_valid.extend(valid)             # إلحاق القيم الصالحة بالقائمة التجميعية
            except Exception: continue                # تجاوز الدوال التي تفشل في الحساب المبدئي بصمت

        x_lo, x_hi = -30, 30                          # تثبيت النطاق الأفقي للرسم بشكل صارم لضمان عدم التجاوز
        if not all_y_valid:                           # التحقق من خلو القائمة من أي قيم صالحة
            y_lo, y_hi = -30, 30                      # تطبيق النطاق الرأسي الأقصى في حالة الفشل
        else:                                         # في حال وجود بيانات صالحة للتحليل
            lo = calculate_percentile(all_y_valid, 5) # استخراج المئين الخامس لتجاهل القيم الشاذة الدنيا
            hi = calculate_percentile(all_y_valid, 95) # استخراج المئين الخامس والتسعين لتجاهل القيم الشاذة العليا
            if hi - lo < 1e-5:                        # التحقق من حالة الدالة الثابتة رياضياً
                lo -= 5                               # إضافة هامش سفلي اصطناعي
                hi += 5                               # إضافة هامش علوي اصطناعي
            ym = max(2.0, (hi - lo) * 0.25 + 2)       # حساب هامش بصري ديناميكي يعتمد على سعة الدالة
            
            y_lo = max(lo - ym, -30)                  # تعيين الحد الرأسي الأدنى مع فرض قيد صارم يمنع النزول تحت -30
            y_hi = min(hi + ym, 30)                   # تعيين الحد الرأسي الأقصى مع فرض قيد صارم يمنع الصعود فوق 30
            
            if y_lo >= y_hi:                          # إجراء حماية إضافي في حال كانت الدالة تقع بالكامل خارج النطاق (مثلاً y = 100)
                y_lo, y_hi = -30, 30                  # إعادة تعيين النطاق الرأسي للقيم القصوى لمنع انهيار مكتبة الرسم

        self.canvas.reset(xlim=(x_lo, x_hi), ylim=(y_lo, y_hi)) # إعادة تهيئة لوحة الرسم بالنطاقات المحسوبة والمقيدة
        
        plot_x = generate_linspace(x_lo, x_hi, 3000)  # توليد فضاء خطي عالي الدقة (3000 نقطة) للرسم النهائي الناعم
        for i, (expr, name) in enumerate(self.functions): # تكرار عملية الرسم الفعلي لكل دالة مسجلة
            color = CURVE_COLORS[i % len(CURVE_COLORS)] # تعيين لون المنحنى من القائمة المخصصة
            try:                                      # محاولة الرسم النهائي المتسامح مع الأخطاء
                sym = sp.sympify(expr.replace("^", "**")) # استخراج التعبير الرمزي مجدداً
                y_vals = lambdify_safe(sym, x_sym, plot_x) # تقييم الدالة بدقة عالية استناداً للفضاء الخطي الجديد
                self.canvas.ax.plot(plot_x, y_vals, label=f"{name}(x) = {expr}", color=color, lw=PlotCanvas.CURVE_WIDTH) # رسم المنحنى المتصل وتوثيق التسمية في مفتاح الرسم
            except Exception: pass                    # تجاوز أي أخطاء متأخرة أثناء الرسم بصمت تام

        self.canvas.ax.legend(loc="best")             # استدعاء مفتاح الرسم البياني واختيار أفضل موقع تلقائي له
        self.canvas.refresh()                         # تحديث الإطار البصري لعرض المنحنيات المنجزة

    def _on_clear(self):                              # تعريف إجراء الاستجابة لمسح كافة الدوال
        self.functions.clear()                        # تفريغ قائمة الدوال المسجلة في الذاكرة
        update_textbox(self.textbox, "")              # مسح كافة النصوص المعروضة في مساحة القائمة
        self.canvas.reset()                           # إعادة تهيئة لوحة الرسم لمسح المنحنيات السابقة


# تبويب حل الجمل الخطية بيانياً  ══════════════════════════════════════════════════════════════════════════════

class SystemTab(ctk.CTkFrame):                        # تعريف فئة لتبويب مخصص لحل جملة معادلتين خطيتين بيانياً
    def __init__(self, parent):                       # تعريف دالة التهيئة للتبويب
        super().__init__(parent, fg_color="transparent") # استدعاء دالة التهيئة للفئة الأصلية بخلفية شفافة
        self._build_ui()                              # استدعاء دالة البناء البصري لمكونات التبويب

    def _build_ui(self):                              # تعريف دالة ترتيب واجهة التبويب
        left = make_sidebar(self, width=268)          # إنشاء اللوحة الجانبية مع تحديد عرض مخصص يتناسب مع المعادلات
        self._build_header(left)                      # بناء الترويسة الوصفية
        self._build_equations_card(left)              # بناء بطاقة إدخال المعادلتين المتقاطعتين
        self._build_ranges(left)                      # بناء بطاقات تحديد نطاقات الرسم
        self._build_action_buttons(left)              # بناء أزرار تنفيذ الحل والمسح

        self.canvas = PlotCanvas(self)                # إنشاء لوحة الرسم المستقلة للتبويب
        self.canvas.pack(side="right", fill="both", expand=True, pady=4) # إدراج وتمديد لوحة الرسم على المساحة المتبقية

    def _build_header(self, p):                       # تعريف دالة بناء الترويسة
        ctk.CTkLabel(p, text="System of Equations", font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT).pack(anchor="w", padx=10, pady=(10, 2)) # إدراج العنوان الأساسي للتبويب
        ctk.CTkLabel(p, text="Form:  ax + by = c  (integers or decimals)", font=ctk.CTkFont(size=11), text_color=MUTED).pack(anchor="w", padx=10, pady=(0, 4)) # إدراج الوصف الرياضي للصيغة المطلوبة
        make_divider(p)                               # إدراج خط فاصل تنظيمي

    def _build_equations_card(self, p):               # تعريف دالة بناء بطاقة إدخال الجملة
        make_section_label(p, "Equations")            # إدراج عنوان قسم المعادلات
        c = make_card(p)                              # توليد كائن البطاقة
        c.pack(fill="x", padx=10, pady=8)             # إدراج البطاقة مع التمدد الأفقي
        c.columnconfigure(1, weight=1)                # تفعيل التمدد التلقائي في الشبكة للحقول النصية

        self.entry_eq1 = make_entry(c, placeholder="2x + y = 5", width=180) # حقل إدخال المعادلة الخطية الأولى
        self.entry_eq2 = make_entry(c, placeholder="x  - y = 1", width=180) # حقل إدخال المعادلة الخطية الثانية

        for i, (label, color, widget) in enumerate([("Eq 1", CURVE_COLORS[0], self.entry_eq1), ("Eq 2", CURVE_COLORS[1], self.entry_eq2)]): # تكرار وتخصيص الألوان لكل معادلة في الشبكة
            ctk.CTkLabel(c, text=label, text_color=color, font=ctk.CTkFont(size=12, weight="bold"), width=44, anchor="e").grid(row=i, column=0, padx=(4, 2), pady=3, sticky="e") # إدراج التسمية الملونة لتتطابق مع لون المنحنى
            widget.grid(row=i, column=1, padx=(2, 6), pady=3, sticky="ew") # إدراج حقل الإدخال في الشبكة

    def _build_ranges(self, p):                       # تعريف دالة بناء بطاقات تحديد النطاقات المكانية للوحة
        self.entry_xmin, self.entry_xmax = build_range_card(p, "x — Abscissas Range", "-10", "10") # بطاقة تحديد مجال المحور السيني
        self.entry_ymin, self.entry_ymax = build_range_card(p, "y — Ordinates Range", "-10", "10") # بطاقة تحديد مجال المحور الصادي

    def _build_action_buttons(self, p):               # تعريف دالة بناء أزرار الأوامر
        make_divider(p)                               # إدراج خط فاصل تنظيمي ختامي
        danger_btn(p, "Clear", self._on_clear, "⊗").pack(fill="x", padx=10, pady=(8, 20), side="bottom") # إدراج زر التفريغ في أسفل اللوحة مع تعزيز الهامش
        primary_btn(p, "Solve & Plot", self._on_solve, "⊜").pack(fill="x", padx=10, pady=(4, 8), side="bottom") # إدراج زر الحل الجبري والرسم البياني

    def _on_solve(self):                              # تعريف إجراء التنفيذ المتسلسل للحل الجبري والرسم
        try:                                          # محاولة استخراج النطاقات المدخلة
            xmin, xmax = read_range(self.entry_xmin, self.entry_xmax) # قراءة النطاق السيني وتأكيد صحته
            ymin, ymax = read_range(self.entry_ymin, self.entry_ymax) # قراءة النطاق الصادي وتأكيد صحته
        except ValueError as err:                     # التقاط خطأ في المنطق الرقمي للنطاقات
            messagebox.showerror("Input Error", str(err)); return # عرض خطأ وإيقاف التنفيذ

        try:                                          # محاولة استخراج وتحليل المعادلات نصياً
            eq1 = parse_equation(self.entry_eq1.get()) # تحويل نص المعادلة الأولى لكائن جبري
            eq2 = parse_equation(self.entry_eq2.get()) # تحويل نص المعادلة الثانية لكائن جبري
        except Exception as err:                      # التقاط خطأ في الصياغة الجبرية
            messagebox.showerror("Parse Error", str(err)); return # عرض خطأ وإيقاف التنفيذ

        x_sym, y_sym = sp.symbols("x y")              # تعريف المتغيرات الرمزية لاستخدامها في الحل الجبري

        try:                                          # محاولة عزل المتغير التابع (ص) تمهيداً للرسم
            y1_sols = sp.solve(eq1, y_sym)            # حل المعادلة الأولى بالنسبة لـ (ص)
            y2_sols = sp.solve(eq2, y_sym)            # حل المعادلة الثانية بالنسبة لـ (ص)
            if not y1_sols or not y2_sols: raise ValueError("Cannot isolate y — ensure each equation contains y.") # إثارة خطأ إذا تعذر استخراج دالة صريحة
            y1_expr, y2_expr = y1_sols[0], y2_sols[0] # تخزين التعابير الصريحة للدوال
        except Exception as err:                      # التقاط أخطاء العزل الجبري
            messagebox.showerror("Algebra Error", str(err)); return # عرض خطأ وإيقاف التنفيذ

        x_sol = y_sol = None                          # تهيئة متغيرات الحل المشترك بقيمة فارغة
        has_solution = False                          # تعيين حالة الحل المبدئية بالنفي
        try:                                          # محاولة إيجاد الحل الجبري المشترك للجملة (نقطة التقاطع)
            sol = sp.solve([eq1, eq2],[x_sym, y_sym]) # توجيه محرك الرياضيات لحل الجملة الخطية
            if isinstance(sol, dict) and x_sym in sol and y_sym in sol: # التأكد من وجود حل وحيد مستقل
                x_sol, y_sol, has_solution = float(sol[x_sym]), float(sol[y_sym]), True # استخراج قيم الحل وتأكيد الحالة
        except Exception: pass                        # تجاهل الأخطاء بصمت في حال التوازي أو التطابق الهندسي

        x_vals = generate_linspace(xmin, xmax, 900)   # توليد فضاء خطي لرسم منحنيات المعادلات
        y1_vals = lambdify_safe(y1_expr, x_sym, x_vals) # حساب قيم الدالة الأولى
        y2_vals = lambdify_safe(y2_expr, x_sym, x_vals) # حساب قيم الدالة الثانية

        self.canvas.reset(xlim=(xmin, xmax), ylim=(ymin, ymax)) # إعادة ضبط اللوحة بالنطاقات المحددة من المستخدم
        self.canvas.ax.plot(x_vals, y1_vals, label=f"Eq1:  y = {sp.simplify(y1_expr)}", color=CURVE_COLORS[0], lw=PlotCanvas.CURVE_WIDTH) # رسم وإدراج المنحنى الأول
        self.canvas.ax.plot(x_vals, y2_vals, label=f"Eq2:  y = {sp.simplify(y2_expr)}", color=CURVE_COLORS[1], lw=PlotCanvas.CURVE_WIDTH) # رسم وإدراج المنحنى الثاني

        if has_solution:                              # التحقق من توفر حل جبري للرسم
            self.canvas.ax.scatter([x_sol], [y_sol], color=AMBER, s=45, zorder=8, edgecolors="white", linewidths=1.0) # إدراج نقطة مبعثرة لتمييز التقاطع
            self.canvas.ax.annotate(                  # بدء إدراج صندوق الشرح النصي لمعالم الحل
                f"  ({x_sol:.3f}, {y_sol:.3f})", (x_sol, y_sol), # تمرير النص المنسق والموقع الجغرافي للنقطة
                xytext=(12, 12), textcoords="offset points", fontsize=10, color=AMBER, fontweight="bold", zorder=9, # ضبط الإزاحة والتنسيق اللوني للخط
                bbox=dict(boxstyle="round,pad=0.5", fc=CARD, ec=AMBER, alpha=0.92) # رسم بطاقة خلفية للنص بحواف دائرية
            )

        self.canvas.ax.legend(loc="best")             # إضافة مفتاح الرسم التوضيحي للمعادلات
        self.canvas.refresh()                         # تحديث الإطار البصري لعرض النتائج

    def _on_clear(self):                              # تعريف إجراء مسح وتفريغ تبويب الجمل الخطية
        self.entry_eq1.delete(0, "end")               # إفراغ محتوى حقل المعادلة الأولى
        self.entry_eq2.delete(0, "end")               # إفراغ محتوى حقل المعادلة الثانية
        self.canvas.reset()                           # تنظيف لوحة الرسم وإعادتها لحالتها الافتراضية



# افئة التطبيق الرئيسية وهيكل الواجهة العام ══════════════════════════════════════════════════════════════════════════════

class App(ctk.CTk):                                   # تعريف فئة التطبيق الرئيسية الموروثة من نافذة واجهة المستخدم
    TITLE    = "Graphical Math Solver"                # تعريف ثابت نصي لعنوان البرنامج الرئيسي
    SUBTITLE = "Alwan Brothers Middle School"         # تعريف ثابت نصي للاسم التعريفي للمالك

    def __init__(self):                               # تعريف دالة التهيئة للنافذة الرئيسية
        super().__init__()                            # استدعاء دالة التهيئة الأساسية لإنشاء كائن النافذة
        self.title(self.TITLE)                        # تعيين العنوان الرئيسي للنافذة في شريط النظام
        self.geometry("1180x720")                     # تحديد الأبعاد الهندسية الافتراضية للنافذة عند الإطلاق
        self.minsize(940, 640)                        # تطبيق قيود دنيا على الأبعاد لمنع تشوه واجهة المستخدم
        self.configure(fg_color=BG)                   # تطبيق اللون المخصص على خلفية النافذة الأساسية
        self._build_topbar()                          # استدعاء إجراء هندسة الترويسة العلوية للبرنامج
        self._build_tabs()                            # استدعاء إجراء هندسة ودمج التبويبات الوظيفية

    def _build_topbar(self):                          # تعريف دالة بناء الترويسة العلوية الثابتة للتطبيق
        bar = ctk.CTkFrame(self, height=56, corner_radius=0, fg_color=PANEL) # إنشاء إطار الترويسة المستطيل بلون مخصص
        bar.pack(fill="x", side="top")                # إدراج الترويسة في الأعلى وتمديدها أفقياً على طول النافذة
        bar.pack_propagate(False)                     # حظر الانكماش التلقائي للترويسة للمحافظة على ارتفاعها الثابت

        ctk.CTkFrame(bar, width=4, fg_color=BLUE, corner_radius=0).pack(side="left", fill="y") # إدراج شريط زينة جانبي لتعزيز الهوية البصرية
        ctk.CTkLabel(bar, text="  Graphical Math Solver", font=ctk.CTkFont(size=18, weight="bold"), text_color=TEXT).pack(side="left", padx=(12, 8), pady=14) # إدراج اسم التطبيق العريض في الترويسة
        ctk.CTkLabel(bar, text=f"·  {self.SUBTITLE}", font=ctk.CTkFont(size=11), text_color=MUTED).pack(side="left", pady=14) # إدراج النص الفرعي الوصفي بجوار العنوان
        secondary_btn(bar, "About", self._open_about, "ⓘ").pack(side="right", padx=14, pady=12, ipadx=10) # إدراج زر المعلومات في أقصى يمين الترويسة

    def _build_tabs(self):                            # تعريف دالة بناء نظام التبويبات المتعددة لإدارة الأقسام
        tabs = ctk.CTkTabview(                        # إنشاء كائن إدارة التبويبات الرسومي
            self, fg_color=BG, segmented_button_fg_color=PANEL, # تطبيق الألوان الأساسية على حاوية التبويبات
            segmented_button_selected_color=BLUE, segmented_button_selected_hover_color=BLUE_H, # تخصيص ألوان زر التبويب النشط
            segmented_button_unselected_color=PANEL, segmented_button_unselected_hover_color=CARD_H, # تخصيص ألوان أزرار التبويبات غير النشطة
            corner_radius=14                          # تطبيق حواف دائرية على شريط التبويبات
        )                                            
        tabs.pack(fill="both", expand=True, padx=12, pady=(6, 12)) # إدراج حاوية التبويبات لتشغل المساحة الرئيسية المتبقية

        tab_defs =[                                   # تهيئة قائمة بتعريفات التبويبات وفئاتها المرتبطة
            ("  ● Points & Lines  ",      PointsTab), # تعريف التبويب الأول المخصص لإدارة النقاط
            ("  ∿ Functions  ",           FunctionsTab), # تعريف التبويب الثاني المخصص للدوال والمنحنيات
            ("  ≡ System of Equations  ", SystemTab), # تعريف التبويب الثالث المخصص لحل الجمل الخطية
        ]                                           
        for name, TabClass in tab_defs:               # بدء حلقة تكرار لإنشاء ودمج التبويبات المحددة
            TabClass(tabs.add(name)).pack(fill="both", expand=True) # إنشاء مثيل من الفئة المخصصة وإدراجه ضمن التبويب المقابل

    def _open_about(self):                            # تعريف دالة استدعاء نافذة المعلومات الفرعية
        AboutWindow(self)                             # تهيئة وإنشاء كائن نافذة المعلومات وربطه بالنافذة الحالية


# تشغيل البرنامج :)  ══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":                            # التحقق من أن الملف يتم تنفيذه كبرنامج رئيسي وليس كوحدة مستوردة
    App().mainloop()                                  # إنشاء مثيل للتطبيق وبدء حلقة الأحداث الرئيسية لواجهة المستخدم
