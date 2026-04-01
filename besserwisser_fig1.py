import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

plt.rcParams.update({'font.family':'serif','mathtext.fontset':'cm',
    'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':300,'font.size':11})

# ── Figure 1: Complexity + Information Gap ────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

ax1.set_xlim(0,10); ax1.set_ylim(0,10)
ax1.set_aspect('equal'); ax1.axis('off')

ax1.add_patch(mpatches.Ellipse((5,5),9.2,8.8,
    facecolor='#e8f4f8',edgecolor='#2c5f7a',lw=2.5))
ax1.add_patch(mpatches.Ellipse((4.2,4.5),4.5,3.8,
    facecolor='#c8e6c9',edgecolor='#2e7d32',lw=2.5))
ax1.text(4.2,4.5,r'$\mathsf{P}$',ha='center',va='center',
         fontsize=26,color='#2e7d32',fontweight='bold')
ax1.text(7.8,8.2,r'$\mathsf{NP}$',ha='center',va='center',
         fontsize=26,color='#2c5f7a',fontweight='bold')
ax1.plot(3.8,4.8,'o',color='#c62828',markersize=13,zorder=5)
ax1.annotate('Besserwisser\n'+r'$\mathcal{B}\in\mathsf{P}$',
    xy=(3.8,4.8),xytext=(0.5,2.2),fontsize=9.5,color='#c62828',
    arrowprops=dict(arrowstyle='->',color='#c62828',lw=1.5))
ax1.plot(7.2,6.5,'s',color='#1565c0',markersize=13,zorder=5)
ax1.annotate('Producer\n'+r'$\text{PROD}\in\mathsf{NP}$',
    xy=(7.2,6.5),xytext=(6.8,3.8),fontsize=9.5,color='#1565c0',
    arrowprops=dict(arrowstyle='->',color='#1565c0',lw=1.5))
ax1.annotate('',xy=(6.4,5.9),xytext=(4.9,5.1),
    arrowprops=dict(arrowstyle='<->',color='#555',lw=2.0,
                    connectionstyle='arc3,rad=0.25'))
ax1.text(5.5,4.8,'structural\ngap',ha='center',fontsize=8.5,
         color='#555',style='italic')
ax1.text(5.0,1.1,
    r'$\mathsf{P}\neq\mathsf{NP}\Rightarrow\nexists\,\mathcal{B}$ solves PROD',
    ha='center',fontsize=9,color='#2c3e50',
    bbox=dict(boxstyle='round,pad=0.4',facecolor='#fffde7',
              edgecolor='#f9a825',lw=1.5))
ax1.set_title(r'$\mathbf{(a)}$  Complexity landscape ($\mathsf{P}\neq\mathsf{NP}$)',
              fontsize=11,pad=10,loc='left')

k = np.arange(1,61)
ax2.fill_between(k,k,alpha=0.2,color='#c62828')
ax2.plot(k,k,color='#c62828',lw=2.5,
         label=r'Besserwisser: $k$ bits')
for ld,c,ls in [(10,'#2e7d32','--'),(20,'#1565c0','--'),(30,'#6a1b9a',':')]:
    ax2.axhline(ld,color=c,lw=2.2,linestyle=ls,
                label=r'Producer: $\log_2|D|=$'+f'${ld}$')
ax2.set_xlabel('Operations $k$',fontsize=11)
ax2.set_ylabel('Information generated (bits)',fontsize=11)
ax2.set_title(r'$\mathbf{(b)}$  Information gap (unconditional)',
              fontsize=11,pad=10,loc='left')
ax2.legend(fontsize=9,frameon=False)
ax2.grid(alpha=0.2); ax2.set_ylim(0,35)

plt.tight_layout(pad=2.0)
plt.savefig('fig1_theory.pdf',bbox_inches='tight')
plt.close()

# ── Figure 2: Stuckness Phase Portrait ───────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

t = np.linspace(0,25,400)
C_bw = 1.8*t + 0.03*t**1.8
I_bw = 0.4 + 0.03*t
S_bw = C_bw - I_bw
C_pr = 1.2*t
I_pr = 0.2*t + 0.07*t**1.35
S_pr = C_pr - I_pr

ax1.plot(t,S_bw,color='#c62828',lw=2.5,label='Besserwisser')
ax1.plot(t,S_pr,color='#1565c0',lw=2.5,label='Producer')
ax1.axhline(0,color='#2e7d32',lw=1.8,linestyle='--',alpha=0.8,
            label=r'$S=0$ (flow)')
ax1.fill_between(t,S_bw,0,where=(S_bw>0),alpha=0.10,color='#c62828')
ax1.fill_between(t,S_pr,0,where=(S_pr<0),alpha=0.10,color='#1565c0')
cross=np.argmin(np.abs(S_pr))
ax1.axvline(t[cross],color='#1565c0',lw=1,linestyle=':',alpha=0.6)
ax1.text(t[cross]+0.4,-8,r'$t^*$: flow onset',fontsize=8.5,color='#1565c0')
ax1.annotate(r'$S\to\infty$',xy=(22,S_bw[-1]),fontsize=10,color='#c62828',
    ha='center',bbox=dict(boxstyle='round,pad=0.3',facecolor='#ffebee',
    edgecolor='#c62828',lw=1))
ax1.annotate(r'$S\to 0$',xy=(20,S_pr[int(20/25*400)]-3),fontsize=10,
    color='#1565c0',ha='center',
    bbox=dict(boxstyle='round,pad=0.3',facecolor='#e3f2fd',
    edgecolor='#1565c0',lw=1))
ax1.set_xlabel('Time (production cycles)',fontsize=11)
ax1.set_ylabel(r'$S=C-I$ (Stuckness Score)',fontsize=11)
ax1.set_title(r'$\mathbf{(c)}$  Stuckness trajectories over time',
              fontsize=11,pad=10,loc='left')
ax1.legend(fontsize=10,frameon=False)
ax1.grid(alpha=0.2)

C_range=np.linspace(0,10,200); I_range=np.linspace(0,10,200)
Cg,Ig=np.meshgrid(C_range,I_range)
Sg=Cg-Ig
cf=ax2.contourf(Cg,Ig,Sg,levels=np.linspace(-8,8,40),cmap='RdBu_r',alpha=0.82)
ax2.contour(Cg,Ig,Sg,levels=[0],colors='black',linewidths=2)
t2=np.linspace(0,1,100)
ax2.plot(1+7*t2,1+0.4*t2,'r-',lw=2.5,label='Besserwisser')
ax2.annotate('',xy=(1+7*t2[-1],1+0.4*t2[-1]),
    xytext=(1+7*t2[-2],1+0.4*t2[-2]),
    arrowprops=dict(arrowstyle='->',color='#c62828',lw=2))
ax2.plot(1+4*t2,0.5+6*t2,'b-',lw=2.5,label='Producer')
ax2.annotate('',xy=(1+4*t2[-1],0.5+6*t2[-1]),
    xytext=(1+4*t2[-2],0.5+6*t2[-2]),
    arrowprops=dict(arrowstyle='->',color='#1565c0',lw=2))
ax2.set_xlabel(r'$C$ (accumulated complexity)',fontsize=11)
ax2.set_ylabel(r'$I$ (integration / output)',fontsize=11)
ax2.set_title(r'$\mathbf{(d)}$  Phase portrait in $(C,I)$ space',
              fontsize=11,pad=10,loc='left')
ax2.legend(fontsize=10,frameon=False,loc='upper left')
ax2.text(6.5,1.5,r'$S>0$',fontsize=13,color='#c62828',alpha=0.8)
ax2.text(1.5,7.5,r'$S<0$',fontsize=13,color='#1565c0',alpha=0.8)
ax2.text(4.0,4.5,r'$S=0$',fontsize=11,color='black',rotation=45,style='italic')
plt.colorbar(cf,ax=ax2,label=r'$S=C-I$',shrink=0.85)

plt.tight_layout(pad=2.0)
plt.savefig('fig2_stuckness.pdf',bbox_inches='tight')
plt.close()
print("Figures done.")
