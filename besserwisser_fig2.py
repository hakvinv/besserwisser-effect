import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'serif','mathtext.fontset':'cm',
    'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':300,'font.size':11})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

t = np.linspace(0,25,400)
C_bw = 1.8*t + 0.03*t**1.8
I_bw = 0.4 + 0.03*t
G_bw = C_bw - I_bw
C_pr = 1.2*t
I_pr = 0.2*t + 0.07*t**1.35
G_pr = C_pr - I_pr

ax1.plot(t, G_bw, color='#c62828', lw=2.5, label='Besserwisser')
ax1.plot(t, G_pr, color='#1565c0', lw=2.5, label='Producer')
ax1.axhline(0, color='#2e7d32', lw=1.8, linestyle='--', alpha=0.8, label=r'$G=0$ (flow)')
ax1.fill_between(t, G_bw, 0, where=(G_bw>0), alpha=0.10, color='#c62828')
ax1.fill_between(t, G_pr, 0, where=(G_pr<0), alpha=0.10, color='#1565c0')
cross = np.argmin(np.abs(G_pr))
ax1.axvline(t[cross], color='#1565c0', lw=1, linestyle=':', alpha=0.6)
ax1.text(t[cross]+0.4, -8, r'$t^*$: flow onset', fontsize=8.5, color='#1565c0')
ax1.annotate(r'$G\to\infty$', xy=(22, G_bw[-1]), fontsize=10, color='#c62828',
    ha='center', bbox=dict(boxstyle='round,pad=0.3',facecolor='#ffebee',edgecolor='#c62828',lw=1))
ax1.annotate(r'$G\to 0$', xy=(20, G_pr[int(20/25*400)]-3), fontsize=10, color='#1565c0',
    ha='center', bbox=dict(boxstyle='round,pad=0.3',facecolor='#e3f2fd',edgecolor='#1565c0',lw=1))
ax1.set_xlabel('Time (production cycles)', fontsize=11)
ax1.set_ylabel(r'$G = C - I$ (competence gap)', fontsize=11)
ax1.set_title(r'$\mathbf{(c)}$  Competence gap over time', fontsize=11, pad=10, loc='left')
ax1.legend(fontsize=10, frameon=False); ax1.grid(alpha=0.2)

C_range = np.linspace(0,10,200); I_range = np.linspace(0,10,200)
Cg, Ig = np.meshgrid(C_range, I_range)
Gg = Cg - Ig
cf = ax2.contourf(Cg,Ig,Gg,levels=np.linspace(-8,8,40),cmap='RdBu_r',alpha=0.82)
ax2.contour(Cg,Ig,Gg,levels=[0],colors='black',linewidths=2)
t2 = np.linspace(0,1,100)
ax2.plot(1+7*t2,1+0.4*t2,'r-',lw=2.5,label='Besserwisser')
ax2.annotate('',xy=(1+7*t2[-1],1+0.4*t2[-1]),xytext=(1+7*t2[-2],1+0.4*t2[-2]),
    arrowprops=dict(arrowstyle='->',color='#c62828',lw=2))
ax2.plot(1+4*t2,0.5+6*t2,'b-',lw=2.5,label='Producer')
ax2.annotate('',xy=(1+4*t2[-1],0.5+6*t2[-1]),xytext=(1+4*t2[-2],0.5+6*t2[-2]),
    arrowprops=dict(arrowstyle='->',color='#1565c0',lw=2))
ax2.set_xlabel(r'$C$ (accumulated complexity)',fontsize=11)
ax2.set_ylabel(r'$I$ (integration / output)',fontsize=11)
ax2.set_title(r'$\mathbf{(d)}$  Phase portrait in $(C,I)$ space',fontsize=11,pad=10,loc='left')
ax2.legend(fontsize=10,frameon=False,loc='upper left')
ax2.text(6.5,1.5,r'$G>0$',fontsize=13,color='#c62828',alpha=0.8)
ax2.text(1.5,7.5,r'$G<0$',fontsize=13,color='#1565c0',alpha=0.8)
ax2.text(4.0,4.5,r'$G=0$',fontsize=11,color='black',rotation=45,style='italic')
plt.colorbar(cf,ax=ax2,label=r'$G=C-I$',shrink=0.85)
plt.tight_layout(pad=2.0)
plt.savefig('fig2_stuckness.pdf',bbox_inches='tight')
print("Done.")
