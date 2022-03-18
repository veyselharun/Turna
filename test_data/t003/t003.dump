
testif:     file format elf64-littleriscv


Disassembly of section .text:

00000000000100b0 <_start>:
   100b0:	00002197          	auipc	gp,0x2
   100b4:	38818193          	addi	gp,gp,904 # 12438 <__global_pointer$>
   100b8:	81818513          	addi	a0,gp,-2024 # 11c50 <_edata>
   100bc:	85018613          	addi	a2,gp,-1968 # 11c88 <_end>
   100c0:	8e09                	sub	a2,a2,a0
   100c2:	4581                	li	a1,0
   100c4:	222000ef          	jal	ra,102e6 <memset>
   100c8:	00000517          	auipc	a0,0x0
   100cc:	17450513          	addi	a0,a0,372 # 1023c <__libc_fini_array>
   100d0:	140000ef          	jal	ra,10210 <atexit>
   100d4:	1b0000ef          	jal	ra,10284 <__libc_init_array>
   100d8:	4502                	lw	a0,0(sp)
   100da:	002c                	addi	a1,sp,8
   100dc:	4601                	li	a2,0
   100de:	0e6000ef          	jal	ra,101c4 <main>
   100e2:	13a0006f          	j	1021c <exit>

00000000000100e6 <_fini>:
   100e6:	8082                	ret

00000000000100e8 <deregister_tm_clones>:
   100e8:	6549                	lui	a0,0x12
   100ea:	67c9                	lui	a5,0x12
   100ec:	c3850713          	addi	a4,a0,-968 # 11c38 <__TMC_END__>
   100f0:	c3878793          	addi	a5,a5,-968 # 11c38 <__TMC_END__>
   100f4:	00e78b63          	beq	a5,a4,1010a <deregister_tm_clones+0x22>
   100f8:	00000337          	lui	t1,0x0
   100fc:	00030313          	mv	t1,t1
   10100:	00030563          	beqz	t1,1010a <deregister_tm_clones+0x22>
   10104:	c3850513          	addi	a0,a0,-968
   10108:	8302                	jr	t1
   1010a:	8082                	ret

000000000001010c <register_tm_clones>:
   1010c:	67c9                	lui	a5,0x12
   1010e:	6549                	lui	a0,0x12
   10110:	c3878593          	addi	a1,a5,-968 # 11c38 <__TMC_END__>
   10114:	c3850793          	addi	a5,a0,-968 # 11c38 <__TMC_END__>
   10118:	8d9d                	sub	a1,a1,a5
   1011a:	858d                	srai	a1,a1,0x3
   1011c:	4789                	li	a5,2
   1011e:	02f5c5b3          	div	a1,a1,a5
   10122:	c991                	beqz	a1,10136 <register_tm_clones+0x2a>
   10124:	00000337          	lui	t1,0x0
   10128:	00030313          	mv	t1,t1
   1012c:	00030563          	beqz	t1,10136 <register_tm_clones+0x2a>
   10130:	c3850513          	addi	a0,a0,-968
   10134:	8302                	jr	t1
   10136:	8082                	ret

0000000000010138 <__do_global_dtors_aux>:
   10138:	8181c703          	lbu	a4,-2024(gp) # 11c50 <_edata>
   1013c:	eb15                	bnez	a4,10170 <__do_global_dtors_aux+0x38>
   1013e:	1141                	addi	sp,sp,-16
   10140:	e022                	sd	s0,0(sp)
   10142:	e406                	sd	ra,8(sp)
   10144:	843e                	mv	s0,a5
   10146:	fa3ff0ef          	jal	ra,100e8 <deregister_tm_clones>
   1014a:	000007b7          	lui	a5,0x0
   1014e:	00078793          	mv	a5,a5
   10152:	cb81                	beqz	a5,10162 <__do_global_dtors_aux+0x2a>
   10154:	6541                	lui	a0,0x10
   10156:	4d850513          	addi	a0,a0,1240 # 104d8 <__EH_FRAME_BEGIN__>
   1015a:	ffff0097          	auipc	ra,0xffff0
   1015e:	ea6080e7          	jalr	-346(ra) # 0 <_start-0x100b0>
   10162:	4785                	li	a5,1
   10164:	80f18c23          	sb	a5,-2024(gp) # 11c50 <_edata>
   10168:	60a2                	ld	ra,8(sp)
   1016a:	6402                	ld	s0,0(sp)
   1016c:	0141                	addi	sp,sp,16
   1016e:	8082                	ret
   10170:	8082                	ret

0000000000010172 <frame_dummy>:
   10172:	000007b7          	lui	a5,0x0
   10176:	00078793          	mv	a5,a5
   1017a:	cf99                	beqz	a5,10198 <frame_dummy+0x26>
   1017c:	65c9                	lui	a1,0x12
   1017e:	6541                	lui	a0,0x10
   10180:	1141                	addi	sp,sp,-16
   10182:	c5858593          	addi	a1,a1,-936 # 11c58 <object.5217>
   10186:	4d850513          	addi	a0,a0,1240 # 104d8 <__EH_FRAME_BEGIN__>
   1018a:	e406                	sd	ra,8(sp)
   1018c:	ffff0097          	auipc	ra,0xffff0
   10190:	e74080e7          	jalr	-396(ra) # 0 <_start-0x100b0>
   10194:	60a2                	ld	ra,8(sp)
   10196:	0141                	addi	sp,sp,16
   10198:	f75ff06f          	j	1010c <register_tm_clones>

000000000001019c <calc>:
   1019c:	1101                	addi	sp,sp,-32
   1019e:	ec22                	sd	s0,24(sp)
   101a0:	1000                	addi	s0,sp,32
   101a2:	87aa                	mv	a5,a0
   101a4:	872e                	mv	a4,a1
   101a6:	fef42623          	sw	a5,-20(s0)
   101aa:	87ba                	mv	a5,a4
   101ac:	fef42423          	sw	a5,-24(s0)
   101b0:	fec42703          	lw	a4,-20(s0)
   101b4:	fe842783          	lw	a5,-24(s0)
   101b8:	9fb9                	addw	a5,a5,a4
   101ba:	2781                	sext.w	a5,a5
   101bc:	853e                	mv	a0,a5
   101be:	6462                	ld	s0,24(sp)
   101c0:	6105                	addi	sp,sp,32
   101c2:	8082                	ret

00000000000101c4 <main>:
   101c4:	1101                	addi	sp,sp,-32
   101c6:	ec06                	sd	ra,24(sp)
   101c8:	e822                	sd	s0,16(sp)
   101ca:	1000                	addi	s0,sp,32
   101cc:	459d                	li	a1,7
   101ce:	4515                	li	a0,5
   101d0:	fcdff0ef          	jal	ra,1019c <calc>
   101d4:	87aa                	mv	a5,a0
   101d6:	fef42623          	sw	a5,-20(s0)
   101da:	fec42783          	lw	a5,-20(s0)
   101de:	0007871b          	sext.w	a4,a5
   101e2:	4785                	li	a5,1
   101e4:	00f71663          	bne	a4,a5,101f0 <main+0x2c>
   101e8:	479d                	li	a5,7
   101ea:	fef42623          	sw	a5,-20(s0)
   101ee:	a819                	j	10204 <main+0x40>
   101f0:	fec42783          	lw	a5,-20(s0)
   101f4:	0007871b          	sext.w	a4,a5
   101f8:	478d                	li	a5,3
   101fa:	00f71563          	bne	a4,a5,10204 <main+0x40>
   101fe:	47a9                	li	a5,10
   10200:	fef42623          	sw	a5,-20(s0)
   10204:	4781                	li	a5,0
   10206:	853e                	mv	a0,a5
   10208:	60e2                	ld	ra,24(sp)
   1020a:	6442                	ld	s0,16(sp)
   1020c:	6105                	addi	sp,sp,32
   1020e:	8082                	ret

0000000000010210 <atexit>:
   10210:	85aa                	mv	a1,a0
   10212:	4681                	li	a3,0
   10214:	4601                	li	a2,0
   10216:	4501                	li	a0,0
   10218:	1780006f          	j	10390 <__register_exitproc>

000000000001021c <exit>:
   1021c:	1141                	addi	sp,sp,-16
   1021e:	4581                	li	a1,0
   10220:	e022                	sd	s0,0(sp)
   10222:	e406                	sd	ra,8(sp)
   10224:	842a                	mv	s0,a0
   10226:	1d0000ef          	jal	ra,103f6 <__call_exitprocs>
   1022a:	67c9                	lui	a5,0x12
   1022c:	c407b503          	ld	a0,-960(a5) # 11c40 <_global_impure_ptr>
   10230:	6d3c                	ld	a5,88(a0)
   10232:	c391                	beqz	a5,10236 <exit+0x1a>
   10234:	9782                	jalr	a5
   10236:	8522                	mv	a0,s0
   10238:	26e000ef          	jal	ra,104a6 <_exit>

000000000001023c <__libc_fini_array>:
   1023c:	7179                	addi	sp,sp,-48
   1023e:	67c5                	lui	a5,0x11
   10240:	6745                	lui	a4,0x11
   10242:	f022                	sd	s0,32(sp)
   10244:	4e870713          	addi	a4,a4,1256 # 114e8 <__init_array_end>
   10248:	4f078413          	addi	s0,a5,1264 # 114f0 <__fini_array_end>
   1024c:	8c19                	sub	s0,s0,a4
   1024e:	ec26                	sd	s1,24(sp)
   10250:	e84a                	sd	s2,16(sp)
   10252:	e44e                	sd	s3,8(sp)
   10254:	f406                	sd	ra,40(sp)
   10256:	840d                	srai	s0,s0,0x3
   10258:	4481                	li	s1,0
   1025a:	4f078913          	addi	s2,a5,1264
   1025e:	59e1                	li	s3,-8
   10260:	00941a63          	bne	s0,s1,10274 <__libc_fini_array+0x38>
   10264:	7402                	ld	s0,32(sp)
   10266:	70a2                	ld	ra,40(sp)
   10268:	64e2                	ld	s1,24(sp)
   1026a:	6942                	ld	s2,16(sp)
   1026c:	69a2                	ld	s3,8(sp)
   1026e:	6145                	addi	sp,sp,48
   10270:	e77ff06f          	j	100e6 <_fini>
   10274:	033487b3          	mul	a5,s1,s3
   10278:	0485                	addi	s1,s1,1
   1027a:	97ca                	add	a5,a5,s2
   1027c:	ff87b783          	ld	a5,-8(a5)
   10280:	9782                	jalr	a5
   10282:	bff9                	j	10260 <__libc_fini_array+0x24>

0000000000010284 <__libc_init_array>:
   10284:	1101                	addi	sp,sp,-32
   10286:	e822                	sd	s0,16(sp)
   10288:	e426                	sd	s1,8(sp)
   1028a:	6445                	lui	s0,0x11
   1028c:	64c5                	lui	s1,0x11
   1028e:	4dc48793          	addi	a5,s1,1244 # 114dc <__preinit_array_end>
   10292:	4dc40413          	addi	s0,s0,1244 # 114dc <__preinit_array_end>
   10296:	8c1d                	sub	s0,s0,a5
   10298:	e04a                	sd	s2,0(sp)
   1029a:	ec06                	sd	ra,24(sp)
   1029c:	840d                	srai	s0,s0,0x3
   1029e:	4dc48493          	addi	s1,s1,1244
   102a2:	4901                	li	s2,0
   102a4:	02891763          	bne	s2,s0,102d2 <__libc_init_array+0x4e>
   102a8:	64c5                	lui	s1,0x11
   102aa:	e3dff0ef          	jal	ra,100e6 <_fini>
   102ae:	6445                	lui	s0,0x11
   102b0:	4e048793          	addi	a5,s1,1248 # 114e0 <__frame_dummy_init_array_entry>
   102b4:	4e840413          	addi	s0,s0,1256 # 114e8 <__init_array_end>
   102b8:	8c1d                	sub	s0,s0,a5
   102ba:	840d                	srai	s0,s0,0x3
   102bc:	4e048493          	addi	s1,s1,1248
   102c0:	4901                	li	s2,0
   102c2:	00891d63          	bne	s2,s0,102dc <__libc_init_array+0x58>
   102c6:	60e2                	ld	ra,24(sp)
   102c8:	6442                	ld	s0,16(sp)
   102ca:	64a2                	ld	s1,8(sp)
   102cc:	6902                	ld	s2,0(sp)
   102ce:	6105                	addi	sp,sp,32
   102d0:	8082                	ret
   102d2:	609c                	ld	a5,0(s1)
   102d4:	0905                	addi	s2,s2,1
   102d6:	04a1                	addi	s1,s1,8
   102d8:	9782                	jalr	a5
   102da:	b7e9                	j	102a4 <__libc_init_array+0x20>
   102dc:	609c                	ld	a5,0(s1)
   102de:	0905                	addi	s2,s2,1
   102e0:	04a1                	addi	s1,s1,8
   102e2:	9782                	jalr	a5
   102e4:	bff9                	j	102c2 <__libc_init_array+0x3e>

00000000000102e6 <memset>:
   102e6:	433d                	li	t1,15
   102e8:	872a                	mv	a4,a0
   102ea:	02c37163          	bleu	a2,t1,1030c <memset+0x26>
   102ee:	00f77793          	andi	a5,a4,15
   102f2:	e3c1                	bnez	a5,10372 <memset+0x8c>
   102f4:	e1bd                	bnez	a1,1035a <memset+0x74>
   102f6:	ff067693          	andi	a3,a2,-16
   102fa:	8a3d                	andi	a2,a2,15
   102fc:	96ba                	add	a3,a3,a4
   102fe:	e30c                	sd	a1,0(a4)
   10300:	e70c                	sd	a1,8(a4)
   10302:	0741                	addi	a4,a4,16
   10304:	fed76de3          	bltu	a4,a3,102fe <memset+0x18>
   10308:	e211                	bnez	a2,1030c <memset+0x26>
   1030a:	8082                	ret
   1030c:	40c306b3          	sub	a3,t1,a2
   10310:	068a                	slli	a3,a3,0x2
   10312:	00000297          	auipc	t0,0x0
   10316:	9696                	add	a3,a3,t0
   10318:	00a68067          	jr	10(a3)
   1031c:	00b70723          	sb	a1,14(a4)
   10320:	00b706a3          	sb	a1,13(a4)
   10324:	00b70623          	sb	a1,12(a4)
   10328:	00b705a3          	sb	a1,11(a4)
   1032c:	00b70523          	sb	a1,10(a4)
   10330:	00b704a3          	sb	a1,9(a4)
   10334:	00b70423          	sb	a1,8(a4)
   10338:	00b703a3          	sb	a1,7(a4)
   1033c:	00b70323          	sb	a1,6(a4)
   10340:	00b702a3          	sb	a1,5(a4)
   10344:	00b70223          	sb	a1,4(a4)
   10348:	00b701a3          	sb	a1,3(a4)
   1034c:	00b70123          	sb	a1,2(a4)
   10350:	00b700a3          	sb	a1,1(a4)
   10354:	00b70023          	sb	a1,0(a4)
   10358:	8082                	ret
   1035a:	0ff5f593          	andi	a1,a1,255
   1035e:	00859693          	slli	a3,a1,0x8
   10362:	8dd5                	or	a1,a1,a3
   10364:	01059693          	slli	a3,a1,0x10
   10368:	8dd5                	or	a1,a1,a3
   1036a:	02059693          	slli	a3,a1,0x20
   1036e:	8dd5                	or	a1,a1,a3
   10370:	b759                	j	102f6 <memset+0x10>
   10372:	00279693          	slli	a3,a5,0x2
   10376:	00000297          	auipc	t0,0x0
   1037a:	9696                	add	a3,a3,t0
   1037c:	8286                	mv	t0,ra
   1037e:	fa2680e7          	jalr	-94(a3)
   10382:	8096                	mv	ra,t0
   10384:	17c1                	addi	a5,a5,-16
   10386:	8f1d                	sub	a4,a4,a5
   10388:	963e                	add	a2,a2,a5
   1038a:	f8c371e3          	bleu	a2,t1,1030c <memset+0x26>
   1038e:	b79d                	j	102f4 <memset+0xe>

0000000000010390 <__register_exitproc>:
   10390:	67c9                	lui	a5,0x12
   10392:	c407b703          	ld	a4,-960(a5) # 11c40 <_global_impure_ptr>
   10396:	832a                	mv	t1,a0
   10398:	1f873783          	ld	a5,504(a4)
   1039c:	e789                	bnez	a5,103a6 <__register_exitproc+0x16>
   1039e:	20070793          	addi	a5,a4,512
   103a2:	1ef73c23          	sd	a5,504(a4)
   103a6:	4798                	lw	a4,8(a5)
   103a8:	487d                	li	a6,31
   103aa:	557d                	li	a0,-1
   103ac:	04e84463          	blt	a6,a4,103f4 <__register_exitproc+0x64>
   103b0:	02030a63          	beqz	t1,103e4 <__register_exitproc+0x54>
   103b4:	00371813          	slli	a6,a4,0x3
   103b8:	983e                	add	a6,a6,a5
   103ba:	10c83823          	sd	a2,272(a6)
   103be:	3107a883          	lw	a7,784(a5)
   103c2:	4605                	li	a2,1
   103c4:	00e6163b          	sllw	a2,a2,a4
   103c8:	00c8e8b3          	or	a7,a7,a2
   103cc:	3117a823          	sw	a7,784(a5)
   103d0:	20d83823          	sd	a3,528(a6)
   103d4:	4689                	li	a3,2
   103d6:	00d31763          	bne	t1,a3,103e4 <__register_exitproc+0x54>
   103da:	3147a683          	lw	a3,788(a5)
   103de:	8e55                	or	a2,a2,a3
   103e0:	30c7aa23          	sw	a2,788(a5)
   103e4:	0017069b          	addiw	a3,a4,1
   103e8:	0709                	addi	a4,a4,2
   103ea:	070e                	slli	a4,a4,0x3
   103ec:	c794                	sw	a3,8(a5)
   103ee:	97ba                	add	a5,a5,a4
   103f0:	e38c                	sd	a1,0(a5)
   103f2:	4501                	li	a0,0
   103f4:	8082                	ret

00000000000103f6 <__call_exitprocs>:
   103f6:	715d                	addi	sp,sp,-80
   103f8:	67c9                	lui	a5,0x12
   103fa:	f44e                	sd	s3,40(sp)
   103fc:	c407b983          	ld	s3,-960(a5) # 11c40 <_global_impure_ptr>
   10400:	f052                	sd	s4,32(sp)
   10402:	ec56                	sd	s5,24(sp)
   10404:	e85a                	sd	s6,16(sp)
   10406:	e486                	sd	ra,72(sp)
   10408:	e0a2                	sd	s0,64(sp)
   1040a:	fc26                	sd	s1,56(sp)
   1040c:	f84a                	sd	s2,48(sp)
   1040e:	e45e                	sd	s7,8(sp)
   10410:	8aaa                	mv	s5,a0
   10412:	8a2e                	mv	s4,a1
   10414:	4b05                	li	s6,1
   10416:	1f89b403          	ld	s0,504(s3)
   1041a:	c801                	beqz	s0,1042a <__call_exitprocs+0x34>
   1041c:	4404                	lw	s1,8(s0)
   1041e:	34fd                	addiw	s1,s1,-1
   10420:	00349913          	slli	s2,s1,0x3
   10424:	9922                	add	s2,s2,s0
   10426:	0004dd63          	bgez	s1,10440 <__call_exitprocs+0x4a>
   1042a:	60a6                	ld	ra,72(sp)
   1042c:	6406                	ld	s0,64(sp)
   1042e:	74e2                	ld	s1,56(sp)
   10430:	7942                	ld	s2,48(sp)
   10432:	79a2                	ld	s3,40(sp)
   10434:	7a02                	ld	s4,32(sp)
   10436:	6ae2                	ld	s5,24(sp)
   10438:	6b42                	ld	s6,16(sp)
   1043a:	6ba2                	ld	s7,8(sp)
   1043c:	6161                	addi	sp,sp,80
   1043e:	8082                	ret
   10440:	000a0963          	beqz	s4,10452 <__call_exitprocs+0x5c>
   10444:	21093783          	ld	a5,528(s2)
   10448:	01478563          	beq	a5,s4,10452 <__call_exitprocs+0x5c>
   1044c:	34fd                	addiw	s1,s1,-1
   1044e:	1961                	addi	s2,s2,-8
   10450:	bfd9                	j	10426 <__call_exitprocs+0x30>
   10452:	441c                	lw	a5,8(s0)
   10454:	01093683          	ld	a3,16(s2)
   10458:	37fd                	addiw	a5,a5,-1
   1045a:	02979663          	bne	a5,s1,10486 <__call_exitprocs+0x90>
   1045e:	c404                	sw	s1,8(s0)
   10460:	d6f5                	beqz	a3,1044c <__call_exitprocs+0x56>
   10462:	31042703          	lw	a4,784(s0)
   10466:	009b163b          	sllw	a2,s6,s1
   1046a:	00842b83          	lw	s7,8(s0)
   1046e:	8f71                	and	a4,a4,a2
   10470:	2701                	sext.w	a4,a4
   10472:	ef09                	bnez	a4,1048c <__call_exitprocs+0x96>
   10474:	9682                	jalr	a3
   10476:	4418                	lw	a4,8(s0)
   10478:	1f89b783          	ld	a5,504(s3)
   1047c:	f9771de3          	bne	a4,s7,10416 <__call_exitprocs+0x20>
   10480:	fcf406e3          	beq	s0,a5,1044c <__call_exitprocs+0x56>
   10484:	bf49                	j	10416 <__call_exitprocs+0x20>
   10486:	00093823          	sd	zero,16(s2)
   1048a:	bfd9                	j	10460 <__call_exitprocs+0x6a>
   1048c:	31442783          	lw	a5,788(s0)
   10490:	11093583          	ld	a1,272(s2)
   10494:	8ff1                	and	a5,a5,a2
   10496:	2781                	sext.w	a5,a5
   10498:	e781                	bnez	a5,104a0 <__call_exitprocs+0xaa>
   1049a:	8556                	mv	a0,s5
   1049c:	9682                	jalr	a3
   1049e:	bfe1                	j	10476 <__call_exitprocs+0x80>
   104a0:	852e                	mv	a0,a1
   104a2:	9682                	jalr	a3
   104a4:	bfc9                	j	10476 <__call_exitprocs+0x80>

00000000000104a6 <_exit>:
   104a6:	4581                	li	a1,0
   104a8:	4601                	li	a2,0
   104aa:	4681                	li	a3,0
   104ac:	4701                	li	a4,0
   104ae:	4781                	li	a5,0
   104b0:	05d00893          	li	a7,93
   104b4:	00000073          	ecall
   104b8:	00055c63          	bgez	a0,104d0 <_exit+0x2a>
   104bc:	1141                	addi	sp,sp,-16
   104be:	e022                	sd	s0,0(sp)
   104c0:	842a                	mv	s0,a0
   104c2:	e406                	sd	ra,8(sp)
   104c4:	4080043b          	negw	s0,s0
   104c8:	00a000ef          	jal	ra,104d2 <__errno>
   104cc:	c100                	sw	s0,0(a0)
   104ce:	a001                	j	104ce <_exit+0x28>
   104d0:	a001                	j	104d0 <_exit+0x2a>

00000000000104d2 <__errno>:
   104d2:	8101b503          	ld	a0,-2032(gp) # 11c48 <_impure_ptr>
   104d6:	8082                	ret
